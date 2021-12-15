#!/usr/bin/env python
# coding: utf-8

# In[32]:


class power:
    def __init__(self,base,Power):
        self.base=base
        self.Power=Power
    def cal_power(self,base,Power):
        print("The value of",self.base,"raised to power of",self.Power,"is:",(self.base**self.Power))
base=int(input())
Power=int(input())
prob=power(base,Power)
prob.cal_power(base,Power)

