class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res = 0
        for num in nums:
            while num > 0:
                if num % 10 == digit:
                    res += 1
                num = num // 10
        return res