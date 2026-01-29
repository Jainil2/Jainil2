class Solution:
    def calc(self, graph):
        n = len(graph)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][k] != 1000000007 and graph[k][j] != 1000000007:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        res = 0
        INF = 1000000007
        graph = [[INF for _ in range(26)] for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        n = len(original)
        for i in range(n):
            s = ord(original[i]) - ord("a")
            d = ord(changed[i]) - ord("a")
            graph[s][d] = min(graph[s][d], cost[i])
        self.calc(graph)
        for i in range(len(source)):
            s = ord(source[i]) - ord("a")
            d = ord(target[i]) - ord("a")
            if graph[s][d] == 1000000007:
                return -1
            res += graph[s][d]
        return res
