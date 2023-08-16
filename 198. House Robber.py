class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = no = 0
        for loot in nums:
            rob, no = no + loot, max(rob, no)
        return max(rob, no)
