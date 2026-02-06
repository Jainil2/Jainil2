class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i, j = 0, 0
        res = float('inf')
        while i < n:
            while j < n and nums[i] * k >= nums[j]:
                j += 1
            res = min(res, n - (j - i))
            i += 1
        return res
