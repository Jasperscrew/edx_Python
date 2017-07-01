# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:13:31 2017

@author: Joe
"""

def dict_invert(d):
    newdic = {} #Intializes inverted dictionary   
    uniquevals = [] #Intializes new dictionary values
    
    for key in d: #Places unique values of d into list
        if d[key] not in uniquevals:
            uniquevals.append(d[key])
    
    for i in uniquevals: #Places unique values as keys in newdic and sets values to empty lists
        newdic[i] = []        

    for e in uniquevals: #Appends the original keys to their matching original values in newdic
                for key,value in d.items():
                    if e == value:
                        newdic[e].append(key)
    
    for key in newdic: #sort values
        newdic[key] = sorted(newdic[key])                    
    return newdic   