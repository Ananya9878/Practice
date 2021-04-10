class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return True
        p = head
        s = set()
        while p.next is not None:
            if p.next not in s:
                s.add(p.next)
            else:
                return False
            p = p.next
        return True


