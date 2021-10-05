class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        quick Sort 3:23-3:40
        compare with pivot 
        use recursion so be careful about base case and return type
        quick sort sort inplace and return None
        '''
        
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
        
    def quick_sort(self, nums, left, right):
        # base case
        if left >= right:
            return 
        # got mid as pivot
        pivot = nums[(left + right) // 2]
        # recursion rule
        i = left
        j = right
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        # left------j-i------right  
        # left to j is smaller than or equal to pivot 
        # i to right is grater than or equal to pivot
        self.quick_sort(nums, i, right)
        self.quick_sort(nums, left, j)
