# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:32:29 2017

@author: Joe
"""

def is_list_permutation(L1,L2):
    if is_empty(L1,L2):
        return (None,None,None)
    elif is_perm(L1,L2):
        return calclargest(L1,L2)
    else:
        return False
                          