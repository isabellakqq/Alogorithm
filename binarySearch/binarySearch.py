class BinarySearch:
    def nextGreatestLetter(self, letters, target: str) -> str:
        '''
        clarify : char arr -> char greater than target
        asscding oder=> has duplicate
        c f f j  target c
        l     h
          m
        h
        '''
        n = len(letters)
        if n == 0:
            return None
        
        low = 0
        high = n - 1
        # If it can not be found, 有可能是0， 或者n，初始化为n是因为在大于target的时候会被修改
        result = n
        
        while low <= high:
            mid = low + (high-low) // 2
            if letters[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return letters[result] if result != n else -1
    
    
        