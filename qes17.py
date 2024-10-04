#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:47:15 2024

@author: student
"""
count = 0
for i in range(100,1000,1):
#checking the base condition

    if i%5==0 or i%6==0:
        count = count + 1
        print(i, end = " ")
        if(count%10==0):
            print("/n")



