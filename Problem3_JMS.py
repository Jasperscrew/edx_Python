# -*- coding: utf-8 -*-
"""
Spyder Editor

@ Joe Saunders
Problem Set 1 - Problem 3
Finds the longest substring of "s" in which the letters occur in alphabetical order
"""

s = "jnuesuppwfpjinj"
alphalist = "abcdefghijklmnopqrstuvwxyz"
strlongest = 1
longeststr = s[0]
for i in range(len(s)-1):
    strcounter = 1
    letindex1 = alphalist.index(s[i])
    longeststrtemp = s[i]
    j = i + 1
    letindex2 = alphalist.index(s[j])
    while letindex1 <= letindex2:
        strcounter +=1
        longeststrtemp = longeststrtemp + s[j]
        if j == len(s)-1:
            break
        letindex1 = letindex2
        j += 1
        letindex2 = alphalist.index(s[j])
    if strcounter>strlongest:
        strlongest = strcounter
        longeststr = longeststrtemp    
        
print("Longest substring in alphabetical order is:",longeststr)