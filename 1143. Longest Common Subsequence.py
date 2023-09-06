class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        scores = [[0 for _ in text2] for _ in text1]
        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                best = 0
                if j > 0:
                    best = max(best, scores[i][j - 1])
                if i > 0:
                    best = max(best, scores[i - 1][j])
                if x == y:
                    best = max(best, 1)
                if j > 0 and i > 0 and x == y:
                    best = max(best, scores[i - 1][j - 1] + 1)
                scores[i][j] = best
        return scores[-1][-1]
