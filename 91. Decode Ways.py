class Solution:
    def numDecodings(self, s: str) -> int:
        this = prev = 1
        for i, c in enumerate(s):
            prev, prev2 = this, prev
            prev_c = s[i-1] if i else ""
            alone = prev * (c != "0")
            group = prev2 * (10 <= int(prev_c + c) <= 26)
            this = alone + group
        return this
