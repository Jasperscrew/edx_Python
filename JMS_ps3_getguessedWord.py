# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:55:57 2017

@author: jms815
"""

secretWord2 = 'apple'
lettersGuessed2 = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):  
    guessedword = ''
    secretwordlist = list(secretWord)
    indeces = []
    for i in lettersGuessed:
       for j in range(len(secretwordlist)):
           if i == secretwordlist[j]:
               indeces.append(j)
    for e in range(len(secretwordlist)):
        if e in indeces:
            guessedword = guessedword + secretwordlist[e]
        else:
            guessedword = guessedword + '_ '
                
    return guessedword

getGuessedWord(secretWord2,lettersGuessed2)