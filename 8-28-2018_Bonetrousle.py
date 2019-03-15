#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:33:23 2018

@author: toby
"""
import os
import sys
import random


#%%
### answer corrected for 10/14 tests
# https://www.hackerrank.com/challenges/bonetrousle/problem
def bonetrousle(n, k, b):
    minV = b*(b+1)/2
    maxV = b*(2*k-b+1)/2 # == sum(range(k-b+1,k+1))

    if n > maxV:
        # print("-1")
        return "-1"
    elif n < minV:
        return "-1"
    else:
        init_result = list(range(1,b+1))
        q = (n-minV)/b
        r = (n-minV)%b
        tmp = [_ + int(q) for _ in init_result]

        for i in range(len(tmp)-int(r),len(tmp)):
            print(i)
            tmp[i] += 1
        return tmp

#%%

n = 1
k = 1
b = 1

minV = b*(b+1)/2
maxV = b*(2*k-b+1)/2 # == sum(range(k-b+1,k+1))

if n > maxV:
    print("-1")

else:
    init_result = list(range(1,b+1))
    q = (n-minV)/b
    r = (n-minV)%b
    tmp = [_ + int(q) for _ in init_result]
    
    for i in range(len(tmp)-int(r),len(tmp)):
        print(i)
        tmp[i] += 1
    print(tmp)



#%%
#def bonetrousle(n, k, b):

def find_box(b_candidates, b_list, remaining_sticks, b):
    if len(b_list) > b:
        return "negative error"
    if remaining_sticks == 0:
        return b_list
    elif remaining_sticks < 0:
        return "negative error"
    else:
        print("len of b_candidates = ", len(b_candidates))
        this_box_id = random.randint(0,len(b_candidates)-1)
        print("box id = ", this_box_id)
        remaining_sticks = remaining_sticks - b_candidates[this_box_id]
        print("continue, picked box = %d, remaining = %d" %(b_candidates[this_box_id], remaining_sticks))
        b_list.append(b_candidates.pop(this_box_id))
        print(b_candidates, b_list)
        return find_box(b_candidates, b_list, remaining_sticks,b)
    
n = 9
k = 10
b = 2
buy = []
max_sticks = sum(range(k-b+1,k+1))
if n > max_sticks:
    print("-1")
else:
    tmp = "negative error"
    count = 0 
    while (tmp== "negative error") and (count <= 1000):
        tmp = find_box(list(range(1, k)),[],n,b)
        count += 1
print("*"*10)
print(tmp, count)
    
    


#%%
r = str(tmp[0])
for i in tmp[1:]:
    r = r + " " + str(i)
r

#%%
    
r = "hum"
for i in range(10):
    tmp = find_box(list(range(1, 8)),[],12)
    if tmp != "negative error":
        r = tmp
        
r
#bonetrousle(12,8,3)  
#%%  
count = 0
while True and (count <= 10):
    count += 1
    print(count)
print("finish")


