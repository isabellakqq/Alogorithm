class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = None
ListNode.__lt__ = lambda x, y: (x.val < y.val)
import heapq
class Solution:
    def mergeK(self,lists):
        dummy = ListNode(0)
        cur = dummy
        q = [] 
        for head in lists:
            if head:
                heapq.heappush(q, head)
               
        while q:
            node = heapq.heappop(q)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(q, node)
            
        return dummy.next
s = Solution()
node = ListNode(1)
node.next = ListNode(4)
node2 = ListNode(3)
node2.next = None
head3 = s.mergeK([node,node2])
while head3:
    print(head3.val)
    head3 = head3.next