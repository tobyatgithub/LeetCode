#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:00:11 2018

@author: toby
"""


s = "pwwkew"

store = list(s)

longest = 0
for i in range(len(store)):
    l = store[i]
    text = l
    print("%d th iteration" %i)
    print("text=", text)
    for words in store[i+1:]:
        print('words=',words)
        if words in text:
            break
        else:
            text += words
    tmp = len(list(text))
    if tmp > longest:
        longest = tmp
    
print(longest)




a = [1,2,3,4]
b = [1,2,3,4,5]

def findMedianSortedArrays(a,b):
    len_a = len(a)
    len_b = len(b)
    if len_a >= len_b:
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a
            
    new = []
    while len(longer) != 0 and len(shorter)!=0:
        if longer[0] < shorter[0]:
            new.append(longer.pop(0))
        else:
            new.append(shorter.pop(0))
        print(new)
    print('while ends with :', new, longer,shorter)
    
    if len(longer) == 0:
        new += shorter
    else:
        new += longer
        
    return new

def findmedian(nums):
    length = len(nums)
    if length > 1:
        if length %2 == 1: #odd
            index = int(length/2)
            return nums[index]
        else:
            index = int(length/2)
            return (nums[index-1] + nums[index])/2
    elif length == 0:
            return (None)
    else:
        return nums[0]    
c = [1,3]
d = [2]    

new = findMedianSortedArrays(c,d)
findmedian(new)

#%%
def exc_or(a,b):
    return (a+b == 1)

def dynamicArray(n, queries):
    s0 = []
    s1 = []
    la = 0
    r = []
    #print(queries)
    for q in queries:
#        print(q,s0,s1)
        if q[0] == 1:
            if exc_or(q[1],la)%2 == 0:
                s0.append(q[-1])
            else:
                s1.append(q[-1])
        else:
            if exc_or(q[1],la)%2 == 0:
                la = s0[la%len(s0)]
#                print("q-1, and size",q[-1],s0, len(s0))
#                print(la,q[-1],len(s0),r)
                r.append(la)                
            else:
                la = s1[la%len(s1)]
#                print("q-1, and size", q[-1],s1, len(s1))
#                print(la,q[-1],len(s1),r)
                r.append(la)
            #print(la)
    return r
t = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
dynamicArray(_,t)



