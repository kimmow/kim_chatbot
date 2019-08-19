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
    if re.match(r'.*([, ...?!\.,!?])$',' '.join(line)):
        return []
    return [', ']

def good_line(line):
    if len(re.findall(r'[a-zA-Z0-9]',' ').join(line))>2:
        return False
    return True