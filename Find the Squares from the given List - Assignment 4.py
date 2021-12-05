#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=input().split() # Taking the input
y=map(lambda x:int(x)*int(x),x) # Using lambda function to return square the value of elements in the list
print(list(y))

