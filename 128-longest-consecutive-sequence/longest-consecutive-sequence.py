class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 0
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] == nums[r - 1]:
                l += 1
                r += 1
                continue
            if nums[r] != nums[r - 1] + 1:
                res = max(res, r - l)
                l = r
            r += 1
        res = max(res, r - l)
        return res