# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 09:01:02 2017

@author: Joe
"""

def is_perm(L1,L2):
    '''L1 and L2 are lists
    Checks to see if L1 and L2 are permutations of one another
    Returns True if they are
    returns false otherwise'''
    L1temp = L1[:]
    L2temp = L2[:]
    
    if len(L1) > len(L2):
        for e in L2:
            if e in L1temp:
                L1temp.remove(e)
        if not L1temp:
            return True
        else:
            return False
    else:
        for e in L1:
            #print(e)
            if e in L2temp:
                L2temp.remove(e)
                #print(L2temp)
        if not L2temp:
            return True
        else:
            return False        