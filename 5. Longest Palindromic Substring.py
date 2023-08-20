class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = (0, 0)
        arr = [[False for _ in s] for _ in s]
        for l in range(len(s)):
            for fst in range(len(s) - l):
                snd = fst + l
                if fst == snd:
                    arr[fst][snd] = True
                elif s[fst] == s[snd]:
                    if fst + 1 == snd:
                        arr[fst][snd] = True
                    else:
                        arr[fst][snd] = arr[fst+1][snd-1]

                if arr[fst][snd] and (snd - fst) > (best[1] - best[0]):
                    best = (fst, snd)
            
        return s[best[0]:best[1]+1]
