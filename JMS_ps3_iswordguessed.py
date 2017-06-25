# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:55:57 2017

@author: jms815
"""
def isWordGuessed(secretWord, lettersGuessed):  
    secretwordlist = list(secretWord)
    for i in lettersGuessed:
        while i in secretwordlist:
            secretwordlist.remove(i)       
    if not secretwordlist:
        return True
    else:
        return False
