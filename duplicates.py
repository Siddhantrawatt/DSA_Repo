class Solution:
    def containsDuplicate(self, nums):
        added = []
        for num in nums:
            if num in added:
                return True
            added.append(num)

        return False