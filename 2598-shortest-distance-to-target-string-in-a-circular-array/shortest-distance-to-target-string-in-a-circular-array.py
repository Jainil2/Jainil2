class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        low = n
        high = -1
        res = n
        for i in range(n):
            if words[i] == target:
                low = min(low, i)
                high = max(high, i)
                if low != n:
                    dist_low = abs(startIndex - low) 
                    res = min(res, dist_low, n - dist_low)
                if high != -1:
                    dist_high = abs(startIndex - high)
                    res = min(res, dist_high, n - dist_high)
        if low == n and high == -1:
            return -1
        return res