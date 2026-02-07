class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        d = 0
        for ch in s:
            if ch == 'b':
                b += 1
            else:
                d = min(d + 1, b)
        return d
