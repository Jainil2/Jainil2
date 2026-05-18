class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        indices = defaultdict(list)

        for i, val in enumerate(arr):
            indices[val].append(i)

        q = deque([(0, 0)]) 
        visited = set([0])

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            neighbors = []

            neighbors.extend(indices[arr[i]])

            if i - 1 >= 0:
                neighbors.append(i - 1)

            if i + 1 < n:
                neighbors.append(i + 1)

            for nxt in neighbors:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

            indices[arr[i]].clear()

        return -1