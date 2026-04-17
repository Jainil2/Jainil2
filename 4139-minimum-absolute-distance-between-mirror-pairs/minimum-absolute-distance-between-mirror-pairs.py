class Solution:
    def reverse(self, num: int) -> int:
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10
        return rev

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        res = float('inf')

        for i, x in enumerate(nums):
            if x in last_seen:
                res = min(res, i - last_seen[x])

            r = self.reverse(x)

            last_seen[r] = i

        return -1 if res == float('inf') else res