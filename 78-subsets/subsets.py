class Solution:
    def solve(self, nums, i, arr, res):
        if i >= len(nums):
            return
        for i in range(i, len(nums)):
            arr.append(nums[i])
            res.append(arr[:])
            self.solve(nums, i + 1, arr, res)
            arr.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        self.solve(nums, 0, [], res)
        return res