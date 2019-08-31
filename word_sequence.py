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
            WordSequence.END_TAG : WordSequence.END,
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


