# first attempt
# timed out
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = end = 0
        best = 0
        char = None

        while start < len(s):
            if s[start] == char:
                start += 1
            else:
                char = s[start]
                k_left = k
                end = start + 1

                while end < len(s):
                    if s[end] != char:
                        if k_left:
                            k_left -= 1
                        else:
                            break
                    end += 1
                
                extent = end - start
                extent += max(0, min(start, k_left))
                best = max(extent, best)
        
        return best


# sliding window
# accepted
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0

        for char in set(s):
            k_used = 0
            removes = iter(s)
            length = 0

            for new in s:
                length += 1
                if new != char:
                    if k_used < k:
                        k_used += 1
                    else:
                        removed = char
                        
                        while removed == char:
                            length -= 1
                            removed = next(removes)
                best = max(best, length)
        
        return best
