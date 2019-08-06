#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-06 17:51
# Modified date : 2019-08-06 18:17
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from feature_extract import FeatureExtract

def write_file(file_name, features):
    f = open(file_name, 'w+')
    f.write('\n'.join(features))
    f.close()

def chi_extract():
    dataer = FeatureExtract()
    features = dataer.CHI(5000)
    write_file("./data/chi.txt", features)

def ig_extract():
    dataer = FeatureExtract()
    features = dataer.IG(5000)
    write_file("./data/ig.txt", features)

def mi_extract():
    dataer = FeatureExtract()
    features = dataer.MI(5000)
    write_file("./data/mi.txt", features)

def df_extract():
    dataer = FeatureExtract()
    features = dataer.DF(5000)
    write_file("./data/df.txt", features)

def run():
    df_extract()
    mi_extract()
    ig_extract()
    chi_extract()

if __name__=='__main__':
    run()
