# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:19:31 2019

@author: aashi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:30:45 2019

@author: aashi
"""

#FOR TEXT 1
#Reading the file in a string variable
def index_terms(str1):
    f=open(str1,'r')
    mystr=f.read()
    #print(mystr)

    #Convert the contents into lower case
    mystr=mystr.lower()
    #print(mystr)


    #Removing numbers
    import re
    mystr=re.sub(r'\d+', '', mystr)
    #print(mystr)

    #Tokenize the string
    from nltk.tokenize import word_tokenize
    tokens=word_tokenize(mystr)
    #print(tokens)

    #Removing Punctuation
    tokens = [word for word in tokens if word.isalpha()]
    #print(tokens)

    #Removing Stopwords
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    words = [w for w in tokens if not w in stop_words]
    #print(words)

    #Stemming
    from nltk.stem.porter import PorterStemmer
    porter = PorterStemmer()
    text = [porter.stem(word) for word in words]
    return text

def uniq(index_t):
    unique = []
    for i in index_t:
        for j in i:
            if j not in unique:
                unique.append(j)
    return unique

def inverted_indx(unique, index_t):
    inv_indx = {}
    for i in unique:
        d = {}
        for j in range(0,10):
            l = []
            l.append(0)
            for k in range(0,len(index_t[j])):
                if i == index_t[j][k]:
                    l[0]+=1
                    l.append(k)
            d[doc[j]] = l
        inv_indx[i] = d
    return inv_indx

doc = ['T1.txt', 'T2.txt', 'T3.txt', 'T4.txt', 'T5.txt', 'T6.txt', 'T7.txt', 'T8.txt', 'T9.txt', 'T10.txt']
index_t = []
for i in doc:
    l = index_terms(i)
    index_t.append(l)
unique = uniq(index_t)
inv_indx = inverted_indx(unique, index_t)




