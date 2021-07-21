 def sqrt(self, x):

        '''
        24
        12
        6
        3
        4
        5
        二分
        '''
        if x == 0:
            return 0
        if x // 2 < 2:
            return 1
        left = 2
        right = x // 2
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid 
            else:
                left = mid
        return left
