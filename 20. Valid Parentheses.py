class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"(": ")", "[": "]", "{": "}"}
        p = []
        for c in s:
            if c in matches:
                p.append(c)
            elif not p or matches[p.pop()] != c:
                return False
        return not p
