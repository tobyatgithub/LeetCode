# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid_finder, end_finder = head, head
        # while end_finder.next and end_finder.next.next:
        #     mid_finder = mid_finder.next
        #     end_finder = end_finder.next.next
        # if end_finder.next:
        #     mid_finder = mid_finder.next
        while end_finder and end_finder.next:
            mid_finder = mid_finder.next
            end_finder = end_finder.next.next
        return mid_finder