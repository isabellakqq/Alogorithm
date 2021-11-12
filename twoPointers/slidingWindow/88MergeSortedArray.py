'''
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''
from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        [1,2,3]
        [4, 5]
        i : scan nums1 from left to right i = m - 1
        j : to scan num2 for left to right j = n - 1
        index: nums[index] is inplace what it should be
        
        while i >= 0 and j >= 0:
            put larger one of them at index 
            move i -= 1
            j -= 1
            
        postprocessing
        if j >= 0: nums1[:index] = nums2[:j]
        
        '''
        
        i = m - 1
        j = n - 1
        index = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
            