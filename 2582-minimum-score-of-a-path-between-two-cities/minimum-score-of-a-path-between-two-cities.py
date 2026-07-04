class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        dist = [float('inf')] * (n + 1)
        pq = []
        heapq.heappush(pq, (0, 1))
        dist[1] = 0
        result = float('inf')
        vis = [False] * (n + 1)
        while pq:
            curr, node = heapq.heappop(pq)
            # print(curr, node, pq)
            for adj, w in graph[node]:
                if not vis[adj]:
                    dist[adj] = curr + w
                    result = min(result, w)
                    # print(result, w)
                    heapq.heappush(pq, (dist[adj], adj))
            vis[node] = True
        return -1 if result == float('inf') else result