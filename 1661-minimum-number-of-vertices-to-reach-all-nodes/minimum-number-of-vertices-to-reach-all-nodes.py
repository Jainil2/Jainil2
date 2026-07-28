class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = [0] * n
        for u, v in edges:
            arr[v] += 1
        res = [i for i in range(n) if arr[i] == 0]
        return res