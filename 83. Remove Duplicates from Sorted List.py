# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # time: O(n)
    # space: O(n)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        seen = [head.val]
        cur = head
        while cur.next:
            if cur.next.val in seen:
                cur.next = cur.next.next
            else:
                seen.append(cur.next.val)
                cur = cur.next
                
        
        return head
# comment: since the input ListNode is sorted, so we don't actually need a cache to save seen nodes.


class Solution:
    # time: O(n)
    # space: O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head