class Solution:
    def rob1(self, nums):
        rob = no = 0
        for loot in nums:
            rob, no = no + loot, max(rob, no)
        return max(rob, no)
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
