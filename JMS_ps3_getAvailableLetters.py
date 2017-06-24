# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 19:52:21 2017

@author: jms815
"""

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    import string
    alpha = list(string.ascii_lowercase)
    remalpha = ''
    for i in lettersGuessed:
        alpha.remove(i)
    for e in alpha:
            remalpha = remalpha + e
    return remalpha   