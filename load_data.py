#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : load_data.py
# Create date : 2019-08-06 18:05
# Modified date : 2019-08-06 18:17
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os, math

class DataLoader:
    def __init__(self):
        self.datafile = 'data/data.txt'
        self.dataset, self.cate_dict = self.load_data()
        self.catetype_dict = {
            '0': '汽车',
            '1': '财经',
            '2': 'IT',
            '3': '健康',
            '4': '体育',
            '5': '旅游',
            '6': '教育',
            '7': '招聘',
            '8': '文化',
            '9': '军事',
        }

    def load_data(self):
        dataset = []
        cate_dict = {}
        for line in open(self.datafile):
            line = line.strip().split(',')
            cate = line[0]
            if cate not in cate_dict:
                cate_dict[cate] = 1
            else:
                cate_dict[cate] += 1
            dataset.append([line[0], [word for word in line[1].split(' ') if 'nbsp' not in word]])
        return dataset, cate_dict
