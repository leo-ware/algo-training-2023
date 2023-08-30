# O(n^2) dynamic programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        score = [1 for _ in nums]
        score[0] = 1
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if x > y:
                    score[i] = max(score[i], score[j] + 1)
        return max(score)
