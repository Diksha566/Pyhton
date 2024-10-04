#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:01:58 2024

@author: student
"""

num = int(input("Enter the number: "))
reverse_num = 0

while num > 0:
    last_digit = num % 10  # Taking the last digit
    reverse_num = reverse_num * 10 + last_digit  # Building the reversed number
    num = num // 10  # Removing the last digit from num

print("Reversed number:", reverse_num)
