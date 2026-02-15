class Solution:
    def check(self, s, k, n):
        i, j = k, k + 1
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        i2, j2 = k, k
        while i2 >= 0 and j2 < n and s[i2] == s[j2]:
            i2 -= 1
            j2 += 1
        if j - i > j2 - i2:
            return [i + 1, j - 1]
        return [i2 + 1, j2 - 1]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        p, q = 0, 0
        for i in range(n):
            x, y = self.check(s, i, n)
            if y - x + 1 > q - p + 1:
                q = y
                p = x
        return s[p: q + 1]