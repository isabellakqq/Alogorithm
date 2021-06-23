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
        # If it can not be found, must be the first element (wrap around)
        result = 0 
        
        while low <= high:
            mid = low + (high-low) // 2
            if letters[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        Print(letters[result]) 
        