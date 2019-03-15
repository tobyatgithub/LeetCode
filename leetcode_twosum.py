#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:06:11 2018

@author: toby
"""

def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    searching = True
    ans = 0
    index = 0
    while searching:
        first = nums[0]
        nums.pop(0)
        for i in nums:
            tmp = i + first
            if tmp == target:
                searching = False
                print('index, nums', index, nums)
                if index == 0:
                    ans = [index, index + 1 + nums.index(i)]
                else:
                    ans = [index, index + 1 + nums.index(i)]
        index += 1
    return ans
        
print(twoSum([3,2,3],6))#[0,2]
print(twoSum([3,2,4],6))#[1,2] 


def diagonalDifference(a):
    #print(a)
    # Complete this function
    dim = len(a)
    dig1 = 0
    dig2 = 0
    for i in range(dim):
            print(i,a[i][i],a[i][-i-1])
            dig1 += a[i][i]
            dig2 += a[i][-i-1]
#    print(dig1-dig2)
    return abs(dig1-dig2)

diagonalDifference(test)

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    num1 = ""
    for i in range(0,len(l1)):
        num1 += str(l1[-i-1])
    num2 = ""
    for j in range(0,len(l2)):
        num2 += str(l2[-j-1])
    res = int(num1) + int(num2)
    to_print = list(str(res))
    return [to_print[-i-1] for i in range(len(to_print))]