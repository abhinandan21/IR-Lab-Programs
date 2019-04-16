# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:10:57 2019

@author: Sidharth
"""

import nltk as n
new_filenames = [
        "T1_processed.txt",
        "T2_processed.txt",
        "T3_processed.txt",
        "T4_processed.txt",
        "T5_processed.txt",
        "T6_processed.txt",
        "T7_processed.txt",
        "T8_processed.txt",
        "T9_processed.txt",
        "T10_processed.txt"
        ]

######getting the document######
D_length=len(new_filenames)
D=[]
for i in new_filenames:
    absolute_path="D:\\NLP\\IR\\Evaluation 1\\processed_docs\\"
    path_new=absolute_path+i
    f = open(path_new,"r+");
    data=f.read()
    D.append(data)

#######finding unique words######
let=[]
for i in D:
    tokens=n.tokenize.word_tokenize(i)
    for j in tokens:
        if j not in let:
            let.append(j)
    
len_unique=len(let)
count=[0]*len_unique

for i in D:
    consider=[]
    i=n.tokenize.word_tokenize(i)
    for j in range(len(i)):
        if i[j] in let and i[j] not in consider:
            k=let.index(i[j])
            count[k]=count[k]+1
            consider.append(i[j])
print(count)

P=[.0]*len_unique
N=len(D)
for i in range(len(count)):
    P[i]=(N-count[i]+0.5)/(count[i]+0.5)

print(P)

q="hello world and report guttenberg"
q_temp=n.tokenize.word_tokenize(q)
rank=[.0]*N
for i in range(len(D)):
    temp=1
    for j in n.tokenize.word_tokenize(D[i]):
        if j in q_temp:
            temp=temp*P[let.index(j)]
    rank[i]=temp

print(rank)
temp_rank=rank
sorted=[]
high=0
for j in range(N):
    for i in range(len(temp_rank)):
        if(temp_rank[i]>temp_rank[high]):
            high=i
    sorted.append(new_filenames[high])
    temp_rank[high]=0

print(sorted)