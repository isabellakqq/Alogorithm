class Node:
    def __init__(self):
        # list of Node
        self.child = [None] * 26
        # cur is word
        self.isWord = False
        
class Trie:

    def __init__(self):
        self.head = Node()
    
    def insert(self, word: str) -> None:
        # record head
        cur = self.head
        for ch in word:
            index = ord(ch) - ord('a')
            # not present
            if not cur.child[index]:
                cur.child[index] = Node()
            # move to child node
            cur = cur.child[index]
        # mark as word
        cur.isWord = True
    
    def search(self, word: str) -> bool:
        cur = self.head
        for ch in word:
            index = ord(ch) - ord('a')
            if not cur.child[index]:
                return False
            cur = cur.child[index]
        return cur.isWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not cur.child[index]:
                return False
            cur = cur.child[index]
        return True
t = Trie()          
t.insert('apple')
t.insert('alle')
t.insert('app')  
print(t.search('app'))
print(t.startsWith('all'))
print(ord('.') - ord('a'))
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)