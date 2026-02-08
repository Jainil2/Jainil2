class Solution:
    def solve(self, nums: List[int], idx: int, temp: List[int], result: List[List[int]]) -> None:
        if idx >= len(nums):
            return
        for idx in range(idx, len(nums)):
            temp.append(nums[idx])
            result.append(temp[:])
            self.solve(nums, idx + 1, temp, result)
            temp.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.solve(nums, 0, [], result)
        return result