import collections
class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value, timestamp])
      
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.d:
            return ''
        # list of pairs
        value_pairs = self.d[key]
        # 如果get的zhi
        if value_pairs[0][1] > timestamp:
                return ''
        else:
            index = self.binary_search(value_pairs, timestamp)
            return value_pairs[index][0]

    def binary_search(self, value_pairs, target):
        left = 0
        right = len(value_pairs) - 1
        res = 0
        while left <= right:
            mid = (left + right) // 2
            
           
            if value_pairs[mid][1] <= target:
                res = mid
                left = mid + 1
                
            else:
                right = mid - 1
        return res
        
            
            
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)