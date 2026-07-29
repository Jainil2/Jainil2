class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        vis = [False] * n

        def dfs(node):
            if node == destination:
                return True
            for adj in graph[node]:
                if not vis[adj]:
                    vis[adj] = True
                    if dfs(adj):
                        return True
            return False
        
        vis[source] = True
        result = dfs(source)
        return result