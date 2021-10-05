class Solution:
    def sortArray(self, nums):
        '''
        mergeSort
        divid and conqure
        time: O(nlogn)
        space: O(n) tmp占了个额外空间
        平衡二叉树 logn层每层合并用O(N)
        '''
        tmp = [0 for _ in range(len(nums))]
        self.merge_sort(nums, 0, len(nums) - 1, tmp)
        return nums
    
    def merge_sort(self, nums, left, right, tmp):
        # base case 
        if left >= right:
            return
        #divid
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid, tmp)
        self.merge_sort(nums, mid + 1, right, tmp)
        # merge
        self.merge(nums, left, right, tmp)
        
    def merge(self, nums, left, right, tmp):
        n = right - left + 1
        mid = (left + right) // 2
        i = left
        j = mid + 1
        for index in range(n):
            if i <= mid and (j > right or nums[i] <= nums[j]):
                tmp[index] = nums[i]
                i += 1
            else:
                tmp[index] = nums[j]
                j += 1
        for index in range(n):
            nums[left + index] = tmp[index]
               
        