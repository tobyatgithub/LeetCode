class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        out = "LinkedList Node: " + str(self.val)
        cur = self.next
        while cur:
            out +=  "->" + str(cur.val)
            cur = cur.next
        out += "  [end]"
        return out
        
    def __str__(self):
        out = "LinkedList Node: " + str(self.val)
        cur = self.next
        while cur:
            out +=  "->" + str(cur.val)
            cur = cur.next
        out += "  [end]"
        return out

    def insert(self, val=0, next=None):
        if self.next is None:
            self.next = ListNode(val=val, next=next)
        else:
            cur = self.next
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val=val, next=next)
        

class LinkedList(object):
    def __init__(self, head):
        # head = ListNode
        self.head = head

    def __repr__(self):
        pass
