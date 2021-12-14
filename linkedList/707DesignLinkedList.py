class Node:
    # 11:48
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
    # single linkedlist use self.size to find tail
    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        # check valid
        if index < 0 or index >= self.size:
            return -1
        # nothing insert 
        if self.head is None:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # check valid
        if index < 0 or index > self.size:
            return 
        # add at head
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            
            new_node.next = cur.next
            cur.next = new_node
        # increment size   
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        # check valid
        if index < 0 or index >= self.size:
            return 
        cur = self.head
        # delete head
        if index == 0:
            self.head = cur.next
        # get pre_node of target node 
        else:
            for _ in range(index - 1):
                cur = cur.next
            
            cur.next = cur.next.next
        # decrese size
        self.size -= 1
        
            
            
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)