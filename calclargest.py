# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 09:16:00 2017

@author: Joe
"""

def calclargest(L1,L2):
    '''L1 and L2 are lists
    finds the largest matching occurance in both lists and
    returns the value, the number of times and the type'''
    largestvar = []
    largesttimes = 0
    for e in L1:
        counter = 0
        for i in L2:
            if e ==i:
                counter+=1
            if counter > largesttimes:
                largesttimes = counter
                largestvar.append(e)
    rlargest = largestvar.pop()
    tlargest = type(rlargest)
    print(tlargest)            
    return (rlargest,largesttimes,tlargest)        