# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:25:16 2019

@author: aashi
"""

import math
d=[['a','b','c','b','d'],['b','e','f','b'],['b','g','c','d'],['b','d','e'],['a','b','e','g'],['b','g','h']]
q=['z','y','z']
al=['a','b','c','d','e','f','g','h']
nw=[]
for i in al:
    c=0
    for j in d:
       if i in j:
           c+=1
    nw.append(c)
#print(nw)
ai=[]
for i in nw:
    c=(6-i+0.5)/(i+0.5)
    ai.append(c)
#print(ai)
r=[]
for i in d:
    pi=1
    for j in i:
        if j in q:
            pi*=ai[al.index(j)]
    r.append(pi)
#print(r)
rank={}
for i in range(0,6):
    d="d("+str(i+1)+")"
    rank[d]=math.log(r[i])
print(rank)