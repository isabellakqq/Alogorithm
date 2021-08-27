
from typing import Collection

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        1:判断出简单图是最短路径直接bfs模版
        2:怎么找找相邻节点:for i  in range(n): left = word[:i],rigth =  word[i+1:],中间枚举26个字母
        3: Optimize : O(1)time to access wordlist use set(wordlist)
        '''
        distance = {beginWord : 1}
        q = Collection.deque([beginWord])
        word_set = set(wordList)
        while q:
            cur = q.popleft()
            if cur == endWord:
                return distance[cur] 
            for neighbor in self.get_next_word(cur):
                if neighbor not in word_set or neighbor in distance:
                    continue
                distance[neighbor] = distance[cur] + 1
                q.append(neighbor)
        return 0
        
    def get_next_word(self, word):
        res = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                res.append(left + char + right)
        return res

        