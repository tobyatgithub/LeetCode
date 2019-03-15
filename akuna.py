#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:44:55 2018

@author: toby
"""

def unusual_sort(numbers):
    """
    perform an sort such that arry[0] < arry[1] > arry[2] < arry[3] ...
    one potential problem is that elements may not necessarily be distinct...and we want </> instead of <=/>= here...
    
    anyway, the idea is, we can check the position one by one, and if condition violated, we swap them.
    """
    for i in range(0, len(numbers)-1):
        if i % 2 == 0:
        # means we are on i = 0, 2, 4, etc positions, where element needs to be smaller than i + 1 element
            if numbers[i] > numbers[i+1]: #check condition, if violate
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        else:
        # means we are on i = 1, 3, 5, etc positions, where element needs to be larger than i + 1 element
            if numbers[i] < numbers[i+1]: #check condition, if violate
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]


    print(numbers)

unusual_sort([1,1,1,2,3])


#%%
    delta = n # initalize the int to store difference between sum and n
    if sum(intList) < n:
        return False #impossible
    elif sum(intList) == n:
        return (0,len(intList))
    else:
        #if we can assume sorted property..this will be much easier, as:
        for i in range(0,len(intList)):
            tmp = [intList[i]]
            ans = (i,i)
            for j in range(i, len(intList)):
                if i != j:
                    # if i ==j, we check the single element array
                    tmp.append(intList[j])
                # check the difference between sum of substrings and N
                tmp_delta = abs(sum(tmp) - n)
                
                # if there're 0 difference, we find the substring, return it
                if tmp_delta == 0:
                    return ans
                # if there's improvement in differnce, save and move on
                if tmp_delta <= delta:
                    delta = tmp_delta
                    ans = (i,j)
                # if there's no improvement in difference, since the string is sorted, we save ans, and check i+1 substring
                else:
                    return ans
                
                
#%%
                    
def find_k_b(pt1,pt2):
    """ given two points, return slop k, and intercept b"""
    
    if (pt2[0]-pt1[0]) == 0:
        return 0, 0
    else:
        k = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        b = pt1[1] - k * pt1[0]
        return k, b

def detect_colinearity(points):
    '''
    Args:
        points: List[List[int]]

    Returns:
        bool
    '''
    # quick check: if there are three points share same x, or three points share same y, return 1
    cache_x = {}
    cache_y = {}
    for p in points:
        # save x labels
        cache_x.setdefault(p[0],0)
        cache_x[p[0]] += 1
        if cache_x[p[0]] >= 3:
            return True
        cache_y.setdefault(p[1],0)
        cache_y[p[1]] += 1
        if cache_y[p[1]] >= 3:
            return True  
    # it's true that i can combine this check into the loop below, but big-O wise this will not change much.
    
    
    # otherwise, we grab two points, and check everyone else whether they are on the same line
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                k, b = find_k_b(points[i],points[j])
                for n in range(len(points)):
                    if (n != i) & (n != j):
                        # we skip the two points we choosed
                        #print("i,j,n", i,j,n)
                        #print("lalala",k, b, points[n])
                        if b == points[n][1] - k * points[n][0]:
                            return True
    return False


def detect_colinearity(points):
    k_b_save = []
    for i in range(0,len(points)):
        for j in range(i,len(points)):
            if i != j:
                k,b = find_k_b(points[i],points[j])
                tmp = (k,b)
                if tmp in k_b_save:
                    return True
                else:
                    k_b_save.append(tmp)
    # if we run through every one and nothing appears,
    return False

t = [
     [0,0],
     [1,1],
     [2,3]
     ]
detect_colinearity(t)