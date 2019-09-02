#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version: 0.1
# @Time    : 2019/8/19 22:32
# @Author  : TongLing
# @File    : word_sequence.py

import numpy as np

class WordSequence:
    PAD_TAG = '<pad>'
    UNK_TAG = '<unk>'
    START_TAG = '<s>'
    EDN_TAG = '</s>'

    PAD = 0
    UNK = 1
    START = 2
    END = 3

    def  __init__(self):
        self.dict = {
            WordSequence.PAD_TAG : WordSequence.PAD,
            WordSequence.UNK_TAG : WordSequence.UNK,
            WordSequence.START_TAG : WordSequence.START,
            WordSequence.END_TAG : WordSequence.END
        }

        self.fited = False

    def to_index(self,word):
        assert self.fited,'WordSequence尚未进行fit操作'
        if word in self.dict:
            return self.dict[word]
        return WordSequence.UNK

    def to_word(self,index):
        assert self.fited,'WordSequence尚未进行fit操作'
        for k,v in self.dict.items():
            if v == index:
                return k
        return WordSequence.UNK_TAG

    def size(self):
        assert self.fited, 'WordSequence尚未进行fit操作'
        return len(self.dict)+1

    def __len__(self):
        return self.size()

    def fit(self,sentences,min_count=5,max_count = None,max_features =None):
        assert not self.fited,"WordSquence只能fit一次"
        count = {}
        for sentence in sentences:
            arr = list(sentence)
            for a in arr:
                if a not in count:
                    count[a] = 0
                count[a] += 1

        if min_count is not None:
            count  = {k:v for k,v in count.items() if v >= min_count}

        if max_count is not None:
            count  = {k:v for k,v in count.items() if v <= max_count}

        self.dict = {
            WordSequence.PAD_TAG: WordSequence.PAD,
            WordSequence.UNK_TAG: WordSequence.UNK,
            WordSequence.START_TAG: WordSequence.START,
            WordSequence.END_TAG: WordSequence.END


        }

        if isinstance(max_features,int):
            count = sorted(list(count.items()),key = lambda x:x[1])
            if max_features is not None and len(count) > max_features:
                count = count[-int(max_features):]
            for w,_ in count:
                self.dict[w] = len(self.dict)
        else:
            for w in sorted(count.keys()):
                self.dict[w] = len(self.dict)


        self.fited = True



