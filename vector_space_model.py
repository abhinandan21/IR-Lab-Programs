# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:30:45 2019

@author: aashi
"""

import inverted_index

def dot(d1,d2):
    sum = 0
    for i in range(0, len(d1)-1):
        sum += d1[i]*d2[i]
    return sum

doc = ['T1.txt', 'T2.txt', 'T3.txt', 'T4.txt', 'T5.txt', 'T6.txt', 'T7.txt', 'T8.txt', 'T9.txt', 'T10.txt']
index_t = []
for i in doc:
    l = inverted_index.index_terms(i)
    index_t.append(l)
unique = inverted_index.uniq(index_t)
inv_indx = inverted_index.inverted_indx(unique, index_t)

freq = []
for i in unique:
     c = 0
     for j in index_t:
         if i in j:
             c+=1
     freq.append(c)

import math
idf = []
for i in freq:
    a = math.log((10/i))/math.log(2)
    idf.append(a)

tf = []
for i in doc:
    l = []
    for j in unique:
        l.append(inv_indx[j][i][0])
    tf.append(l)

wij = []
for i in tf:
    l = []
    for j in range(0,len(i)):
        l.append(i[j]*idf[j])
    wij.append(l)

# 10 X 10 matrix:
lengths = [] # stores the lengths of all the documents
for i in wij:
    sum = 0
    for j in i:
        sum += j*j
    lengths.append(math.sqrt(sum))
matrix = []
for i in range(0, len(doc)):
    l = []
    sum = 0
    for j in range(0, len(doc)):
        l.append(dot(wij[i],wij[j])/(lengths[i]*lengths[j]))
    matrix.append(l)
    
    

    