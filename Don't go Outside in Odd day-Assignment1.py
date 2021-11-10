#!/usr/bin/env python
# coding: utf-8

# # Don't go Outside in Odd day

# In[7]:


c=[]
while(1):
    i=input()
    if(i!=""):
        c.append(i)
    else:
        break
count=0
for i in c:
    if(int(i) & 1):
        count+=1
print(count,len(c)-count)

