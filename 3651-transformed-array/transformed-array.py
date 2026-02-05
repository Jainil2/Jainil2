class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] > 0:
                idx = (i + nums[i]) % n
                result[i] = nums[idx]
            elif nums[i] < 0:
                idx = (i - abs(nums[i])) % n
                result[i] = nums[idx]
            else:
                result[i] = nums[i]
        return result