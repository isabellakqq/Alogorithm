# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        '''
        Exponential growth
        1 - 2 range
        2 - 4 range
        4 - 8 range if target < reader[8] then Binary Saerch in 4 - 8
        8 - 16 range 
        log2(target)
        
        '''
        if target == reader.get(0):
            return 0
        start, end = 1, 1
    
        while target > reader.get(end):
            start = end
            end *= 2
        return self.binarySearch(reader, start, end, target)
    def binarySearch(self, reader, start, end, target):
    
        left, right = start, end
        while left <= right:
            mid = (left + right) // 2 
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        return - 1

