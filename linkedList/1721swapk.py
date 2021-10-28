# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node1 = None
        node2 = None
        
        cur = head
        lens = 0
        
        while cur:
            lens += 1
            
            # move until last k
            if node2:
                node2 = node2.next
                
            # find node1, make node2 move from head
            if lens == k:
                node1 = cur
                node2 = head
            # move cur
            cur = cur.next
            
        # swap
        node1.val, node2.val = node2.val, node1.val

        return head
                
        