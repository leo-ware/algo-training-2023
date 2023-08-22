class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        mx = mn = 1
        for num in nums:
            if num:
                vals = [num*mx, num*mn, num]
                mx = max(vals)
                mn = min(vals)
                best = max(best, mx)
            else:
                mx = mn = 1
                best = max(best, 0)
        
        return best
