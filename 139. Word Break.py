class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # make trie
        words = {"node": False}
        for word in wordDict:
            d = words
            for c in word:
                if c not in d:
                    d[c] = {"node": False}
                d = d[c]
            d["node"] = True
                
        # find working substrings
        breaks = [False for _ in s]
        for i in range(len(s)):
            if (not i) or breaks[i-1]:
                d = words
                for j in range(i, len(s)):
                    c = s[j]
                    if c in d:
                        if d[c]["node"]:
                            breaks[j] = True
                        d = d[c]
                    else:
                        break

        return breaks[-1]
