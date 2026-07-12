class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        import heapq

        n = len(arr)
        heap = []

        for i, val in enumerate(arr):
            heapq.heappush(heap, (val, i))

        rank = 0
        prev = None
        ans = [0] * n

        while heap:
            val, idx = heapq.heappop(heap)

            if val != prev:
                rank += 1
                prev = val

            ans[idx] = rank

        return ans