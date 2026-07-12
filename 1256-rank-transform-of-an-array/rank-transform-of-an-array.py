class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        nums = [(arr[i], i) for i in range(len(arr))]
        nums.sort()

        result = [0] * len(arr)

        rank = 1
        prev = nums[0][0]
        result[nums[0][1]] = rank

        for val, idx in nums[1:]:
            if val != prev:
                rank += 1
                prev = val
            result[idx] = rank

        return result