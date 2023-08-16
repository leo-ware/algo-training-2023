class Solution:
    def climbStairs(self, n: int) -> int:
        this = 1
        one = two = 0
        
        for _ in range(n):
            one += this
            two += this
            this, one, two = one, two, 0
        
        return this
