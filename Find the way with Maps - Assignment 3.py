#!/usr/bin/env python
# coding: utf-8

# In[13]:


x=input().split() # Taking the input
y=map(lambda x:3*int(x),x) # Using lambda function to return triple value of elements in the list
print(list(y))

