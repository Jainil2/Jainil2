class Solution:
    def reverse(self, num):
        return int(str(num)[::-1])

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev = defaultdict(int)
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] in rev:
                res = min(res, i - rev[nums[i]])
            r = self.reverse(nums[i])
            rev[r] = i
        return -1 if res == len(nums) else res
