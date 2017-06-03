# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:23:48 2017

@author: Joe Saunders
"""

s = "My name is Joseph Saunders"
vcounter = 0
for i in range(len(s)):
    if s[i] == "a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        vcounter += 1
print("Number of vowels:",vcounter)        