#!/usr/bin/env python
# coding: utf-8

# In[159]:


from konlpy.tag import Okt
from collections import OrderedDict
import numpy as np
import json
from math import log10

def f(t, d):
    return d.count(t)

def tf(t, d):
    return 0.5 + 0.5*f(t,d)/max([f(w,d) for w in d])

def idf(t, D):
    # D is documents == document list
    numerator = len(D)
    denominator = 1 + len([ True for d in D if t in d])
    return log10(numerator/denominator)

def tfidf(t, d, D):
    return tf(t,d)*idf(t, D)


with open('vsm_over100.json','r',encoding="utf8") as file:
    vsm = json.load(file)
print(len(vsm))
    
data = []
count = 0

size = 1000
score = np.zeros(size*10,dtype = int)

for i in range(10):
    rate = i+1
    file ='rating{}_docs.json'.format(i+1)
    with open(file,encoding = "utf-8") as data_file:
        da = json.load(data_file, object_pairs_hook=OrderedDict)
        for m in range(len(da)):
            if(m == size):
                break
            score[count+m] = rate
        count += len(da[0:size])
        data += da[0:size]

num_data = len(data)
print(num_data)
result = np.zeros((len(vsm),num_data),dtype = float)


for i in range(len(data)):
    if(i%size == 0):
        print(i)
    for j in range(len(data[i])):
        if data[i][j] in vsm:
               result[vsm.index(data[i][j])][i] = tfidf(data[i][j],data[i],data)

np.savetxt("tfidf.csv",result,delimiter=",")
            


# In[115]:


import pickle
import json
file = open("vsm.txt","rb")
c = pickle.load(file)
file.close

print(len(c))

new_vsm = []

for key, val in c.items():
    if val > 500:
        new_vsm.append(key)

print(len(new_vsm))
with open('vsm_over500.json','w',encoding="utf8") as f:
    json.dump(new_vsm,f,ensure_ascii=False)


# In[ ]:


from konlpy.tag import Okt
from collections import OrderedDict
import numpy as np
import json
from math import log10

def f(t, d):
    return d.count(t)

def tf(t, d):
    return 0.5 + 0.5*f(t,d)/max([f(w,d) for w in d])

def idf(t, D):
    # D is documents == document list
    numerator = len(D)
    denominator = 1 + len([ True for d in D if t in d])
    return log10(numerator/denominator)

def tfidf(t, d, D):
    return tf(t,d)*idf(t, D)

with open('vsm_over.json','r',encoding="utf8") as f:
    vsm = json.load(f)


