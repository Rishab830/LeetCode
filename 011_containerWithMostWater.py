from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        curr_max = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] > height[right]:
                prev_right = right
                right -= 1
                while height[right] < height[prev_right]:
                    right -= 1
            else:
                prev_left = left
                left += 1
                while height[left] < height[prev_left]:
                    left += 1
            curr_max = max(curr_max, min(height[left], height[right]) * (right - left))
        return curr_max