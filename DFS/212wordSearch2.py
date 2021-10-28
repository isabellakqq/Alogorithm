DIRECTIONS = (-1, 0), (0, 1), (0, -1), (1, 0)

class Solution:
    def findWords(self, board, words):
        
        trie = self.get_trie(words)
        
        res = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                self.dfs(i, j, trie, set(), board, res)
                
                      
        return res
    
    
    def dfs(self, i, j, parent, visited, board, res):
        if "#" in parent:
            res.append(parent["#"])
            del parent["#"]
            
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
    
        
        if board[i][j] not in parent:
            return
        
        
        if (i, j) in visited:
            return
    
        visited.add((i, j)) 
        
        child = parent[board[i][j]]
        
        
        for delta_x, delta_y in DIRECTIONS:
            x, y = i + delta_x, j + delta_y
            
            self.dfs(x, y, child, visited, board, res)
        
        
        visited.remove((i, j))
        
        if not child:
            del parent[board[i][j]]
            
            
    def get_trie(self, words):
        trie = {}
        
        for word in words:
            node = trie
            
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                    
                node = node[ch]
                
            node["#"] = word
                
        return trie