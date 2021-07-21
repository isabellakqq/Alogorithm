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
        for node in lists:
            if node:
                heapq.heappush(q, (node.val, node))
               
        while q:
            val, ln = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            ln = ln.next
            if ln:
                heapq.heappush(q, (ln.val, ln))
            
        return dummy.next
s = Solution()
node = ListNode(1, ListNode(2, ListNode(3, None)))
node2 = ListNode(2, ListNode(4, None))
print(s.mergeK([node,node2]))