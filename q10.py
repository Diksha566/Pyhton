#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:30:41 2024

@author: student
"""

s = input("Enter a string")
n = len(s)
for i in range(n):
    sub_s=''
    for j in range (i,n):
        sub_s +=s[j]
        print (sub_s)