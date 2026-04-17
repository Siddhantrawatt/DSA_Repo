class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pmax = nums[0]
        pmin = nums[0]
        result = nums[0]

        for i in range (1,len(nums)):
            n = nums[i]

            temp = max(n,pmax*n,pmin*n)
            pmin = min(n,pmax*n,pmin*n)

            pmax = temp

            if pmax > result:
                result = pmax
        
        return result
