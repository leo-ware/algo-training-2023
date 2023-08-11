from collections import deque

# O(n) solution
# maybe a little complicated
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        counts = {}
        needs = set(t_count.keys())
        
        substring = deque()
        best = None
        adds = iter(s)

        s_start = s_end = 0

        while True:
            if needs:
                try:
                    new = next(adds)
                except StopIteration:
                    break
                
                s_end += 1
                substring.append(new)
                counts[new] = counts.get(new, 0) + 1
                if new in needs:
                    if counts[new] >= t_count[new]:
                        needs.remove(new)
            else:
                if (best is None) or (len(substring) < (best[1] - best[0])):
                    best = (s_start, s_end)
                
                out = substring.popleft()
                s_start += 1
                counts[out] -= 1
                if counts[out] < t_count.get(out, 0):
                    needs.add(out)
        
        best = best or (0, 0)
        return s[best[0]:best[1]]
