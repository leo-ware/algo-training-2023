class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = float("-inf")

        while left < right:
            size = min(height[left], height[right]) * (right - left)
            best = max(best, size)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return best
