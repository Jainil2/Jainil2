class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x, total = 0, 0
        while n:
            t = n % 10
            if t != 0:
                x = x * 10 + t
                total += t
            n = n // 10
        x2 = 0
        while x:
            x2 = x2 * 10 + x % 10
            x = x // 10
        return x2 * total