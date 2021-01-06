# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:03:40 2020

@author: Owner
"""
import pandas as pd

df = pd.read_csv('mfcc_data_12.csv')
df = df.drop(['filename'],axis=1)

def get_alike_pairs(num_pairs,index):
    """Generates a list of 2-tuples containing pairs of dataset IDs belonging to the same speaker."""

    pairs = df.loc[df['label'] == index].sample(num_pairs)
    pairs = pairs.to_numpy()
    pairs = (pairs[0],pairs[1])
    return pairs

def get_diff_pairs(num_pairs):
    pairs = df.sample(num_pairs)
    
    while len(pairs['label'].unique()) < 2:
        pairs = df.sample(num_pairs)

    return pairs

a = get_alike_pairs(2,19)
print(len(a))
'''
t = df['label'].unique()
#print(df['label'])
tr = t[10:]
a = get_alike_pairs(4,19)
print(a)
val = t[:10]
'''
