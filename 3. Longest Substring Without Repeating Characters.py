class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        chars = set()
        removes = iter(s)

        for candidate in s:
            while candidate in chars:
                chars.remove(next(removes))
            chars.add(candidate)
            best = max(best, len(chars))
        
        return best
