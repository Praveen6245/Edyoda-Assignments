#!/usr/bin/env python
# coding: utf-8

# # Lets Play With Fibonacci

# In[ ]:


a=0
b=1
while(1):
    c = a + b
    a = b
    b = c
    if(b<=50):
        print(b)

