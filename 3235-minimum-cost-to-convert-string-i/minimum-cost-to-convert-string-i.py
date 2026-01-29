class Solution:
    def calc(self, graph):
        n = len(graph)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][k] + graph[k][j] < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        INF = 10**15
        res = 0

        graph = [[INF for _ in range(26)] for _ in range(26)]

        for i in range(26):
            graph[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            s = ord(o) - ord("a")
            d = ord(c) - ord("a")
            graph[s][d] = min(graph[s][d], w)

        self.calc(graph)

        for s_char, t_char in zip(source, target):
            s = ord(s_char) - ord("a")
            d = ord(t_char) - ord("a")
            if graph[s][d] == INF:
                return -1
            res += graph[s][d]

        return res
