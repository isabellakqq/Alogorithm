# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    time: O(nlogn)
    O(logn) extra space due to recursive call stack. 
    '''
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        next_head = mid.next
        mid.next = None
        return self.merge(self.sortList(head), self.sortList(next_head))
    
    def find_mid(self, head):
        s = head
        f = head
        while f.next and f.next.next:
            f = f.next.next
            s = s.next
        return s
    
    def merge(self, n1, n2):
        dummy = ListNode(0)
        cur = dummy
        while n1 and n2:
            if n1.val < n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
            cur = cur.next
        #n1走完了n2还有要接上
        cur.next = n1 or n2
        return dummy.next

        
        