# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:31:56 2021

@author: barkq
"""

def binarysearch(tab, x):
    low = 0
    high = len(tab)-1

    while low <= high:
        mid = (low+high)
        guess = tab[mid]
        
        if guess == x:
            return mid
        
        if guess > x:
            high = mid - 1
        else:
            low = mid + 1
    return None


t = [5,10,15,20,25]

print(binarysearch(t, 15))
        