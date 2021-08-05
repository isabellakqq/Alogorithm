class ListNode:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next
'''
pre(None) -> 1 -> 2 -> 3 -> 4
None <- 1 <- 2 <- 3 <- 4
solution2:recursion
 
'''    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
class Solution2:
    def reverseLinkList(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverseLinkList(self, head.next)
        head.next.next = head
        head.next = None
        return newHead




