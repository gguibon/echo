#!/usr/bin/python

import numpy as np
import argparse, sent_analysis

sa = sent_analysis.Echo() #there are different initialization options. model=path , etc.

list_test = ['I get the feeling','Yup we can do this !! Come on !', 'yes ! I\'m proud to be a dummy list']
l_results = sa.getResult(list_test, corpus="tw")
for r in l_results:
    print r

# use this code below to have an idea of the time needed for 10K tweets
'''
import pandas as pd
df_text = pd.read_csv("./input/test_10k.tsv", sep="\t", encoding='utf8')
list_entree = df_text['fulltext'] 
for r in sa.getResult(list_entree, corpus="tw"):
    print r
'''