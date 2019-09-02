#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version: 0.1
# @Time    : 2019/8/19 21:32
# @Author  : TongLing
# @File    : extract_conv.py

import re
import sys
import pickle
from tqdm import tqdm

def make_split(line):
    if re.match(r'.*([,...?!\.，！？])$',' '.join(line)):
        return []
    return [', ']

def good_line(line):
    if len(re.findall(r'[a-zA-Z0-9]',' ').join(line))>2:
        return False
    return True

def regular(sen):
    sen = re.sub(r'\.{3,100','...',sen)
    sen = re.sub(r'...{2,100}','...',sen)
    sen = re.sub(r'[,]{1，100}','，',sen)
    sen = re.sub(r'[\.]{1，100}', '。', sen)
    sen = re.sub(r'[\?]{1，100}', '？', sen)
    sen = re.sub(r'[！]{1，100}', '！', sen)

    return sen

def main(limit=20,x_limit=3,y_limit=6):

