class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
  
  
class LinkedList:
    def __init__(self, head=None):
        self.head = head
  
    def __str__(self):
        
        # defining a blank res variable
        res = ""
          
        # initializing ptr to head
        ptr = self.head
          
       # traversing and adding it to res
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
  
       # removing trailing commas
        res = res.strip(", ")
          
        # chen checking if 
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"
  
  
if __name__ == "__main__":
    
    # defining linked list
    ll = LinkedList()
  
    # defining nodes
    node1 = Node(10)
    node2 = Node(15)
    node3 = Node(20)
  
    # connecting the nodes
    ll.head = node1
    node1.next = node2
    node2.next = node3
      
    # when print is called, by default 
    #it calls the __str__ method
    print(ll)