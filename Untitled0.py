
# coding: utf-8

# In[6]:

import pip


# In[7]:

def install(package):
   pip.main(['install', package])


# In[8]:

install('arff') 


# In[11]:

import arff, numpy as np


# In[20]:

dataset = arff.load(open('input\emo_large.arff','r'));
print(dataset['attributes'])

#dataset contains two arrays namely 'attributes' and 'data'.'data' is 
#  a multidimensional array..


# In[26]:



# In[26]:




# In[26]:




# In[ ]:



