class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before, same, after = [], [], []
        for num in nums:
            if num < pivot:
                before.append(num)
            elif num == pivot:
                same.append(num)
            else:
                after.append(num)
        before.extend(same)
        before.extend(after)
        return before