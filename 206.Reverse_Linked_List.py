# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1, iterate with stack 
class Solution:
    # time: O(2n) -> O(n)
    # space: O(n) for stack
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        
        out = cur = ListNode()
        while stack:
            cur.next = stack.pop(-1)
            cur = cur.next
        cur.next = None
        return out.next

# Solution 2, read once and change along the way
class Solution:
    # time: O(n)
    # space: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

# Solution 3, recursive
class Solution:
    # time: O(n)
    # space: O(n) due to recursive stack, which can go n levels deep
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head # bottom
        p = reverseList(head.next) # reverse all the parts after head
        head.next.next = head
        head.next = None # need it for the last recurisve call to remove the loop
        return p
        