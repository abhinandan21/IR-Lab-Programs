# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:58:25 2019

@author: aashi
"""

rq = ['d3','d5','d9','d25','d39','d44','d56','d71','d89','d94','d105','d119','d124','d136','d144']
aq = ['d123','d84','d56','d6','d8','d9','d511','d129','d187','d25','d38','d48','d250','d113','d44','d99','d95','d214','d136','d39','d128','d25','d71','d14','d5']

r = []
p = []
c = 0
for i in range(0,len(aq)):
    if aq[i] in rq:
        c+=1
        r.append(c*100/15)
        p.append(c*100/(i+1))
import matplotlib.pyplot as plt
plt.scatter(r,p)
plt.plot(r,p)
plt.xlabel("recall")
plt.ylabel("precission")
plt.show()

#Average precission for first 4 relevent documents retrived:

avg4 = (p[0]+p[1]+p[2]+p[3])/4


#R-Precission
c = -1
for i in range(0,15):
    if aq[i] in rq:
        c+=1
r_pre = p[c]

f = []
e = []
for i in range(0,len(r)):
    f.append(2/((1/r[i])+(1/p[i])))
    
print("avg4 = "+str(avg4))