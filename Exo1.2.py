# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:07:24 2021

@author: Pc
"""

#Nombre neper
e=1
n=int(input("Saisir un entier strictement positif:  "))
while n<=0:
    n=int(input("saisir un entier strictement positif: "))
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    e+=1/fact
print("Le nombre neper est sensiblement égal à: ", e)