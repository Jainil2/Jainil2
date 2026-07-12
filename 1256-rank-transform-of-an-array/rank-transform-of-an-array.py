class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]