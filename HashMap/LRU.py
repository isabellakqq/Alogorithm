class Node:
    '''
    head -> node1->node2 ->node3 ...->tail
    head.next 是Least Recently Used (LRU) cache. tail.pre是recently used
    '''
    def __init__(self, k, v) -> None:
        self.key = k
        self.val = v
        self.pre = None
        self.next = None
class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
    def _add(self, node):
        p = self.tail.pre
        p.next = node
        node.next = self.tail
        node.pre = p
        self.tail.pre = node

    def _remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p
    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1
    def put(self, key, value):
        #处理put要细心，如果key存在要删了
        if key in self.dict:
            self._remove(self.dict[key])
        #插入尾巴节点update val 不存在也是同样的操作 new一个新node插入尾节点
        newNode = Node(key, value)
        self.dict[key] = newNode
        self._add(newNode)
        #如果超出capacity要删除头节点并且删除字典对应的key-value pair
        if len(self.dict) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dict[n.key]
        

       