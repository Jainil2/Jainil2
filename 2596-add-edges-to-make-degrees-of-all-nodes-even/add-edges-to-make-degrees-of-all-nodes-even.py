class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n + 1)]
        degree = [0] * (n + 1)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1

        odd = [i for i in range(1, n + 1) if degree[i] % 2]

        if len(odd) == 0:
            return True

        if len(odd) == 2:
            u, v = odd

            # Can directly connect u and v?
            if v not in graph[u]:
                return True

            # Try an intermediate vertex
            for x in range(1, n + 1):
                if x != u and x != v:
                    if x not in graph[u] and x not in graph[v]:
                        return True
            return False

        if len(odd) == 4:
            a, b, c, d = odd

            return (
                (b not in graph[a] and d not in graph[c]) or
                (c not in graph[a] and d not in graph[b]) or
                (d not in graph[a] and c not in graph[b])
            )

        return False