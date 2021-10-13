class Solution:
    def sortArray(self, nums):
        
        '''
        dfs(arr, index):
            return : root is reference of TreeNode
            recursion way 
            

        Physical meaning： array ->可以 o(1)time  find l and r child
            index 0 1 2 3 4 
            value 2 3 7 5 4
        Heap is an unsorted array but have special rule to follow 
                   3
              /        \
            4            5
        /       \      /    \   
        5       7    null
         任意节点小于后裔，最小的在根上
         compelete tree:every level is fully filled 最后一层往左边挤
         index of left child = index of parent * 2
         index of right child = index of parent * 2 + 1 = node
         insert: last left then swap up O(logn) time Percolate up/down
         update:o(logn) 
         get/top:o(1)
         pop:o(logn)  把最后一个元素放在top然后swap down
         从最后一个有child的节点开始heapify
  Input data: 4, 10, 3, 5, 1    => 1 3 4 5 10
  
   time: O(nlogn)  space o(1)
          4(0)
        /   \
     10(1)   3(2)
    /   \
 5(3)    null
 
 
 
        10(0)
        /   \
     5(1)    3(2)             10]
    /   \
4(3)    1(4)

         5(0)
        /   \
     4(1)    3(2)              .. 4, 5,10]
    /   
1(3)



         5(0)
        /   \
     4(1)    3(2)
    /   
1(3)
...

        1(0)
        

         
        '''
        self.heapSort(nums)
        return nums
    def heapSort(self, nums):
        def heapify(nums, n, i): 
            l = 2 * i + 1
            r = 2 * i + 2
			
            largest = i
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]: 
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0) 