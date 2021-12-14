def sortColors(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [2,3,2,1,1,0,3,0]
        p0
        p1
        p2
                   
       
        """
        
        p0 = 0
        p1 = 0
        p2 = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                p1 = max(p1, p0)
                p2 = max(p2, p1)
                
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
                p2 = max(p2, p1)

            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 += 1

        return nums
arr = [2,3,2,1,1,0,3,0]
print(sortColors(arr))
                

