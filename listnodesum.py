#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:16:27 2018

@author: toby
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_ln(x):
        l = [x.val]
        while x.next != None:
            l.append(x.next.val)
            x = x.next
        print(l)

def print_ln(x):
    l = [x.val]
    while x.next != None:
        l.append(x.next.val)
        x = x.next
    print(l)
    
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

#print_ln(l1)
#print_ln(l2)    
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    list1 = [l1.val]
    list2 = [l2.val]
    while l1.next != None:
        list1.append(l1.next.val)
        l1 = l1.next
        #print(num1)
    while l2.next != None:
        list2.append(l2.next.val)
        l2 = l2.next            
    print(list1,type(list1),type(list1[0]))
    num1 = ""
    for i in range(0,len(list1)):
        num1 += str(list1[-i-1])
    num2 = ""
    for j in range(0,len(list2)):
        num2 += str(list2[-j-1])
        
    res = int(num1) + int(num2)
    to_print = list(str(res))       
    to_print2 = [int(to_print[-i-1]) for i in range(len(to_print))]
    print(to_print2,type(to_print2)) #by far correct
    
    if len(to_print2) > 0:
        l3 = ListNode(int(to_print2.pop(0)))
        tmp = l3
        #print("ops",to_print2)
        while to_print2 != []:
            print("ops",to_print2)
            tmp.next = ListNode(int(to_print2.pop(0)))
            tmp = tmp.next
    else:
        l3 = ListNode(0)
    return l3

l3 = addTwoNumbers(l1,l2)
print_ln(l3)

ll = ListNode(0)
ll.next = ListNode(1)
tmp = ll.next
tmp.next = ListNode(2)
tmp = tmp.next
tmp.next = ListNode(3)
#print_ln(ll)


#
#
#
#
#
#
#
#     
#class Solution:
#    def addTwoNumbers(self, l1, l2):
#        """
#        :type l1: ListNode
#        :type l2: ListNode
#        :rtype: ListNode
#        """
#        list1 = [l1.val]
#        list2 = [l2.val]
#        while l1.next != None:
#            list1.append(l1.next)
#            l1 = l1.next
#            #print(num1)
#        while l2.next != None:
#            list2.append(l2.val)
#            l2 = l2.next            
#        print(list1,type(list1),type(list1[0]))
#        num1 = ""
#        for i in range(0,len(list1)):
#            num1 += str(list1[-i-1])
#        num2 = ""
#        for j in range(0,len(list2)):
#            num2 += str(list2[-j-1])
#            
#        res = int(num1) + int(num2)
#        to_print = list(str(res))       
#        to_print2 = [int(to_print[-i-1]) for i in range(len(to_print))]
#        print(to_print2)
#        
#        l3 = ListNode(to_print2.pop(0))
#        l3.next = int(to_print2[0])
#        while len(to_print2)>1:
#            l3.value = to_print2.pop(0)
#            l3.next = to_print2[0]
#        return l3
#    
##    addTwoNumbers(x,l1,l2)    