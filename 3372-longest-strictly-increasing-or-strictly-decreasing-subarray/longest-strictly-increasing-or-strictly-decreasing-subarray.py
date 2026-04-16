class Solution:
    def helper(self, arr):
        l, r = 0, 1
        res = 1
        while r < len(arr):
            if arr[r] < arr[r - 1]:
                res = max(res, r - l + 1)
            else:
                l = r
            r += 1
        return res

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        if len(nums) <= 1:
            return len(nums)
        return max(self.helper(nums), self.helper(nums[::-1]))