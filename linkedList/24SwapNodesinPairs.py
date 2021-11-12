# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        DFS: time O(N), space: O(N)
        iterative: time O(N), space: O(1)
        '''
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        
        pre = dummy
        
        while head and head.next:
            
            # node need to be swaped
            
            node1 = head
            node2 = head.next
            
            # swap
            #易错： pre
            pre.next = node2
            
            node1.next = node2.next
            
            node2.next = node1
        
            # move
            pre = node1
            
            head = node1.next
            
        return dummy.next

# recursion写法     
        
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         '''
#         adjacent: if not head or not head.next:return head
#         swap pair by pair
#         '''
#         if not head or not head.next:
#             return head
        
#         cur = head
#         nt = head.next
        
#         tmp = self.swapPairs(nt.next)
        
#         nt.next = cur
#         cur.next = tmp
        
#         return nt