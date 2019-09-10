#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version: 0.1
# @Time    : 2019/9/10 22:39
# @Author  : TongLing
# @File    : data_utils.py

import random
import numpy as np
from tensorflow.python.client import device_lib
from word_sequence import WordSequence

def _get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU'    ]

if __name__ == '__main__':
    print(_get_available_gpus())