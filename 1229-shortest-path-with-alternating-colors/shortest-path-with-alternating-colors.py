class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]):

        graph = [defaultdict(list), defaultdict(list)]

        for u, v in redEdges:
            graph[0][u].append(v)

        for u, v in blueEdges:
            graph[1][u].append(v)

        ans = [-1] * n
        visited = [[False] * 2 for _ in range(n)]

        q = deque([
            (0, 0),   
            (0, 1)   
        ])

        visited[0][0] = True
        visited[0][1] = True

        dist = 0

        while q:
            for _ in range(len(q)):
                node, last = q.popleft()

                if ans[node] == -1:
                    ans[node] = dist

                next_color = 1 - last

                for nei in graph[next_color][node]:
                    if not visited[nei][next_color]:
                        visited[nei][next_color] = True
                        q.append((nei, next_color))

            dist += 1

        return ans