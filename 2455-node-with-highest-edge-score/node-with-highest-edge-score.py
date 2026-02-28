class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        arr = [0] * n
        for i in range(n):
            arr[edges[i]] += i
        res, cur = 0, arr[0]
        for i in range(n):
            if arr[i] > cur:
                res = i
                cur = arr[i]
        return res