# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:22:28 2017

@author: Joe
"""

def round_10(x,base=10):
    '''
    Rounds number to the closest base
    Default base is 10
    '''
    return int(base*round(float(x)/base))

def findbalance(balance,annualinterestrate,payment):
    '''
    Finds the remaining balance after 12 months of constant monthly payments
    balance: balance of money
    annualinterestrate: annual interest rate
    payment: monthly payment
    '''
    i = 0
    while i <12:
        balafterpay = balance - payment
        interestaccrue = balafterpay*(annualinterestrate/12)
        balance  = balafterpay + interestaccrue
        i +=1
    return balance    

balance = 3926
annualInterestRate = 0.2

high = balance
low = 0
epsilon = 10
guesspay = balance

while (high-low)>epsilon:
    tempbal = findbalance(balance,annualInterestRate,guesspay)
    if tempbal <= 0:
        high = guesspay
        guesspay = round_10(low+(high-low)/2)
    else:
        low = guesspay
        guesspay = round_10(low+(high-low)/2)
if high > guesspay:
    guesspay = high
print("Lowest Payment:",guesspay)        