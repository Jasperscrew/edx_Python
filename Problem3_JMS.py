# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:22:28 2017

@author: Joe
"""
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

balance = 999999
annualInterestRate = 0.18

high = (balance*((1+annualInterestRate)**12))/12
low = balance/12
epsilon = 0.01
guesspay = balance

while (high-low)>epsilon:
    tempbal = findbalance(balance,annualInterestRate,guesspay)
    if tempbal <= 0:
        high = guesspay
        guesspay = round(low+(high-low)/2,3)
    else:
        low = guesspay
        guesspay = round(low+(high-low)/2,3)
if high > guesspay:
    guesspay = high
guesspay = round(guesspay,2)    
print("Lowest Payment:",guesspay)        
