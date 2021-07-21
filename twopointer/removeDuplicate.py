 def removeDuplicates(self, nums):
        # write your code here
        '''
        [1,2,2,3]
        同向双指针
        i + 1 
        is final answer semantic meaning
        j index to scan the strif from left to right to find diffrent n with  nums[i]
        '''
        if len(nums) == 1:
            return 1
        if not nums: 
          return 0 
        i = 0 
        n = len(nums)
        for j in range(n): 
          if nums[i] != nums[j]: 
            nums[i + 1] = nums[j] 
            i += 1 
        return i + 1 
