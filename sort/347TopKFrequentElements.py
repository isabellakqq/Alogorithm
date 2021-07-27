import collections
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if len(nums) < k or len(nums) == 1:
        #     return nums
        # cnt = collections.Counter(nums)
        # print(cnt)
        # '''
        # {1:3, 2:2, 3:1, 4 : 2}
        # '''
        # res = []
        # for key, value in cnt.items():
        #     heapq.heappush(res, (value, key))
        #     if len(res) > k:
        #         heapq.heappop(res)
        # return [key for value, key in res]
        '''
        筒排序
        [ []3 ,[2, 4] ,1]
            1      2   3
        '''
#         bucket = [[] for _ in range(len(nums) + 1)]
#         Count = Counter(nums).items()  
#         for num, freq in Count: bucket[freq].append(num) 
#         flat_list = list(chain(*bucket))
#         print(flat_list)
#         return flat_list[::-1][:k]
        '''
        There are solution, using quickselect with O(n) complexity in average, but I think they are overcomplicated: actually, there is O(n) solution, using bucket sort. The idea, is that frequency of any element can not be more than n. So, the plan is the following:

        Create list of empty lists for bucktes: for frequencies 1, 2, ..., n.
        Use Counter to count frequencies of elements in nums
        Iterate over our Counter and add elements to corresponding buckets.
        buckets is list of lists now, create one big list out of it.
        Finally, take the k last elements from this list, these elements will be top K frequent elements.
        Complexity: time complexity is O(n), because we first iterate over nums once and create buckets, then we flatten list of lists with total number of elements O(n) and finally we return last k elements. Space complexity is also O(n).
        '''
        buckets = [[] for _ in range(len(nums) + 1)]
        number_count = collections.Counter(nums)
        for num, freq in number_count.items():
            buckets[freq].append(num)
        # buckets is a double array
        flat_list = []
        # traverse from right to left so number with higher frequency come first
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    flat_list.append(num)
        return flat_list[:k]