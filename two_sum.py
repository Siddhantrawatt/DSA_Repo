# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Your solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = len(nums)
        for i in range (x):
            for j in range (i+1, x):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []