# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 08:58:12 2017

@author: Joe
"""

def is_empty(L1,L2):
    '''L1 and L2: lists containing integers or strings
    returns True if both lists are empty
    returns False if both are not'''
    if not L1 and not L2:
        return True