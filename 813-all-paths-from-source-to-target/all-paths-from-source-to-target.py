class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        s, d = 0, n - 1
        res = []    
        def dfs(node, cur):
            if node == n - 1:
                res.append(cur[:])
                return
            
            for adj in graph[node]:
                cur.append(adj)
                dfs(adj, cur)
                cur.pop()
        dfs(0, [0])
        return res