class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)

        while left + 2 <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            
            if (
                nums[0] <= nums[pivot] < target or
                nums[pivot] < target < nums[0] or
                target < nums[0] <= nums[pivot]
                ):
                left = pivot
            else:
                right = pivot
        
        return -1
