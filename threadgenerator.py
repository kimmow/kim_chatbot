#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version: 0.1
# @Time    : 2019/9/10 21:12
# @Author  : TongLing
# @File    : threadgenerator.py

from threading import Thread
from queue import Queue

class ThreadedGenerator:
    def __init__(self,iterator,
                 sentinel=object(), # 传进一个对象,对象是有效的
                 queue_maxsize=0, # 队列最大的默认值
                 daemon=False):
        self._iterator = iterator
        self._sentinel = sentinel
        self._queue = Queue(maxsize=queue_maxsize)
        self._thread = Thread(
            name=repr(iterator),
            target = self._run
        )
        self._thread.daemon = daemon
        self._started = False

    def __repr__(self):
        return 'ThreadedGenerator({!r})'.format(self._iterator)

    def _run(self):
        try:
            for value in self._iterator:
                if not self._started:
                    return
                self._queue.put(value)
        finally:
            self._queue.put(self._sentinel)

    def close(self):
        self._started = False
        try:
            while True:
                self._queue.get(timeout=30)
        except KeyboardInterrupt as e:
            raise e
        except:
            pass

    def __iter__(self):
        self._started = True
        self._thread.start()
        for value in iter(self._queue.get,self._sentinel):
            yield value
        self._thread.join()
        self._started = False

    def __next__(self):
        if not self._started:
            self._started = True
            self._thread.start()
        value = self._queue.get(timeout =30)
        if value == self._sentinel:
            raise StopIteration()
        return value

def ptest():
    def gene():
        i = 0
        while True:
            yield i
            i += 1
    t = gene()
    test = ThreadedGenerator(t)

    for _ in range(20):
        print(next(test))

if __name__ == '__main__':
    ptest()