class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            pivot = (left + right) // 2
            if nums[pivot] < nums[0]:
                right = pivot
            else:
                left = pivot

        return nums[right]
