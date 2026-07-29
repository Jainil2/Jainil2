class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        q = []
        start = 0
        dist[start] = 0
        heapq.heappush(q, (0,start))

        while q:
            cur_dist, node = heapq.heappop(q)
            
            if dist[node] < cur_dist:
                continue
            
            for adj, w in graph[node]:
                t = cur_dist + w
                if t < dist[adj]:
                    dist[adj] = t
                    heapq.heappush(q, (t, adj))

        result = [0]
        vis = [0] * n

        def dfs(node, score, time, result):

            if node == 0:
                result[0] = max(score, result[0]) 

            for adj, w in graph[node]:
                if time + w > maxTime:
                    continue
                
                if time + w + dist[adj] > maxTime:
                    continue

                if vis[adj] == 0:
                    new_score = score + values[adj]
                else:
                    new_score = score
                vis[adj] += 1
                dfs(adj, new_score, time + w, result)
                vis[adj] -= 1
        vis[0] = 1
        dfs(0, values[0], 0, result)
        return result[0]
