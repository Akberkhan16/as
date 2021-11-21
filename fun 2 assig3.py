#!/usr/bin/env python
# coding: utf-8

# In[17]:


char='The quick Brow Fox'

def case (char):
    upper=0
    lower=0
    for i in char:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    print("No. of upper case characters:",upper)
    print("No. of lower case characters:",lower)
case(char)


# In[ ]:




