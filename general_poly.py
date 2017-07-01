# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:01:32 2017

@author: Joe
"""

def general_poly(L1):
    def polyexp(y):
        total = 0
        len_list = len(L1)
        counter = 0
        for e in L1:
            total = total + e*(y**(len_list-counter-1))
            counter +=1
            print(total)
        return total    
    return polyexp        