def get_max_freq(nums, k):
    if not nums:
        return 0
    nums.sort()
    res = 0
    start, end = 0, 0
    cur_sum = 0
    while end < len(nums):
        cur_sum += nums[end]
        while nums[end] * (end - start + 1) - cur_sum > k:
            cur_sum -= nums[start]
            start += 1
        res = max(res, end - start + 1)
        end += 1
    return res
arr = [-2, 8, 9, -1, -3] 
print(get_max_freq(arr, 5))