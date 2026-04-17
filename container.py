class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width

            if area > max_water:
                max_water = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water