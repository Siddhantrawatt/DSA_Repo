class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)

        curr_max = 0
        max_sum = nums[0]
        curr_min = 0
        min_sum = nums[0]

        for n in nums:
            curr_max = max(n, curr_max + n)
            max_sum = max(max_sum, curr_max)
            curr_min = min(n, curr_min + n)
            min_sum = min(min_sum, curr_min)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)