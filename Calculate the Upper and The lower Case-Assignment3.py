#!/usr/bin/env python
# coding: utf-8

# In[18]:


def cal_case(input_string):
    Upper_count=0 #Variable to store count of upper case letters
    Lower_count=0 #Variable to store count of lower case letters
    for i in input_string:
        if(i.isupper()):# To check if the character is upper case or not
            Upper_count+=1
        else:# Adds the character in lower case count
            Lower_count+=1
    print("No.of Upper case characters :",Upper_count)
    print("No.of Lower case characters :",Lower_count)
input_string=input() # Function_call
cal_case(input_string)

