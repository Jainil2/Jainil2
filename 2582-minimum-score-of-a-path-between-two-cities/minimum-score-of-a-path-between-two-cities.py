class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        visited[1] = True
        stack = [1]
        result = float('inf')

        while stack:
            node = stack.pop()
            for adj, w in graph[node]:
                result = min(result, w)
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)

        return result