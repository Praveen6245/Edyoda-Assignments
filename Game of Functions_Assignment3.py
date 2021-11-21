#!/usr/bin/env python
# coding: utf-8

# In[8]:


def list_sum(l):
    sum=0 # Variable to store the sum of list elements
    for i in range(len(l)):
        sum+=int(l[i])
    print(sum)
l=list((input().split(" "))) # Storing the elements into list after splitting with spaces
list_sum(l)

