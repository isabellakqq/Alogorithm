class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [None for _ in range(16)]
        self.size = 0
        # Ensure optimal space and performance
        self.load_factor = 0.75

    def put(self, key: int, value: int) -> None:
        
        """
        O(1) amortized time 
        value will always be non-negative.
        """
        index = key % len(self.buckets)
        
        head = self.buckets[index]
        # 找有没有
        while head != None and head.key != key:
            head = head.next
        # 找到了更新value
        if head != None:
            head.value = value
        # 插入在头节点更新该index下对应的head
        else:
            newNode = Node(key, value)
            newNode.next = self.buckets[index]
            self.buckets[index] = newNode
            self.size += 1
        
        if self.size >= len(self.buckets) * self.load_factor:
            self._expand()
        

    def get(self, key: int) -> int:
        """
        o(1)
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        index = key % len(self.buckets)
        
        head = self.buckets[index]
        
        while head != None and head.key != key:
            head = head.next
            
        return -1 if head == None else head.value
    

    def remove(self, key: int) -> None:
        """
        O(1) 
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % len(self.buckets)
        head = self.buckets[index]
        
        dummy = Node(0, 0)
        cur = dummy
        dummy.next = head
        while cur.next != None and cur.next.key != key:
            cur = cur.next
        # 找到删除用dummy.next 保留头节点
        if cur.next != None and cur.next.key == key:
            cur.next = cur.next.next
            self.size -= 1
    
        self.buckets[index] = dummy.next
        
    def _expand(self):
        # o(size)
        self.size = 0
        old_buckets = self.buckets
        new_buckets = [None for _ in range(2 * len(self.buckets))]
        self.buckets = new_buckets
        
        for head in old_buckets:
            while head != None:
                self.put(head.key, head.value)
                head = head.next

