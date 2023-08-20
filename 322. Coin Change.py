class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        cache = [float("inf")] * (amount + 1)
        for c in coins:
            if c < len(cache):
                cache[c] = 1
        for a in range(amount + 1):
            for c in coins:
                cache[a] = min(cache[max(0, a - c)] + 1, cache[a])

        return cache[a] if cache[a] != float("inf") else -1
