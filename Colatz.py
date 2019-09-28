# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:57:53 2019
Perform Collatz operation
@author: Eamonn
"""


n = 20
#keep loopimg until we reach 1
while n != 1:
    #if even
    if n % 2 == 0:
        n = n/2
    else:
        #if odd multiply by 3 and add 1
        n = (3* n) + 1
        
print(n)
        
