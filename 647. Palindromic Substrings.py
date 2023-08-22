class Solution:
    def countSubstrings(self, s: str) -> int:
        grid = [[0 for _ in s] for _ in s]
        for length in range(len(s)):
            for i in range(len(s)- length):
                j = i + length
                if i + 1 < j:
                    grid[i][j] = s[i] == s[j] and grid[i + 1][j - 1]
                else:
                    grid[i][j] = s[i] == s[j]
        
        return sum(sum(row) for row in grid)
