#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:31:59 2020

@author: subham
"""

def find_min_max(nums):
    no = 0
    n = len(nums)
    max = nums[0]
    min = nums[0]
    
    for i in range(1, n):
        m = 0
        no += 1
        if nums[i] >= max:
            max = nums[i]
            m = 1
        if m == 0:
            no += 1
            if nums[i] < min:
                min = nums[i]
    return max, min, no

print(find_min_max([3, 5, 1, 2, 4, 8]))