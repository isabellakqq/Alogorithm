import collections
class Solution:
    def alienOrder(self, words) -> str:
        indegree = {}
        graph = collections.defaultdict(set)
        n = len(words)
        # build graph (n * m) m =len(string), n = len(words)
        for i in range(n-1):
            if not self.build(words[i], words[i + 1], graph):
                return ''
        
        # initialize indegree
        for w in words:
            for ch in w:
                indegree[ch] = 0
                
        # update indegree
        # for k , v in hashmap.items()
        for node, neighbor in graph.items():
            for n in neighbor:
                indegree[n] += 1

        # topological sort
        start_nodes = [n for n in indegree if indegree[n] == 0]
        q = collections.deque(start_nodes)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) == len(indegree):
            return ''.join(res)
        else:
            return ''
            
        
    def build(self, str1, str2, graph):
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                graph[str1[i]].add(str2[j])
                return True # aba ab
            i += 1
            j += 1
            
        if len(str1) > len(str2):
            return False
        return True
s = Solution()
test = s.alienOrder(['ba', 'ba'])
print(test)