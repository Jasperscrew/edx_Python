# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:37:02 2017

@author: Joe
"""

# Problem Set 2, Problem 1
# Find remaining balance after 1 year, assuming only paying minimum monthly
# balance

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(0,12):
    minpay = balance*monthlyPaymentRate
    balafterpay = balance - minpay
    interestaccrued = balafterpay*(annualInterestRate/12)
    balance = balafterpay + interestaccrued
balance = round(balance,2)
print("Remaining balance:",balance)    