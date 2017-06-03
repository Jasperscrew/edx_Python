# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:32:40 2017

@author: Joe Saunders
"""

s = "jndbobbboobnbobbbobobooobobobtobobobooboobboobxbo"
bobcounter = 0
for i in range(len(s)):
#    if i!=len(s) and i!=len(s)-1:
        if s[i]=="b" and (i+1)!=len(s) and (i+1)!=len(s)-1:
            if s[i+1]=="o":
                if s[i+2]=="b":
                    bobcounter += 1
print("Number of times bob occurs is:",bobcounter)                