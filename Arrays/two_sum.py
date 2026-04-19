# Problem - Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = len(nums)
        for i in range (x):
            for j in range (i+1, x):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []