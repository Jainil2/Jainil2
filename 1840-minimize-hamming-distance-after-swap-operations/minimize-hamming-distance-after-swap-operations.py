class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            if self.ranks[rootx] > self.ranks[rooty]:
                self.parents[rooty] = rootx
            elif self.ranks[rootx] < self.ranks[rooty]:
                self.parents[rootx] = rooty
            else:
                self.parents[rooty] = rootx
                self.ranks[rootx] += 1

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for u, v in allowedSwaps:
            uf.union(u, v)

        graph = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            graph[root].append(i)

        res = 0
        for indices in graph.values():
            freq = Counter()

            for i in indices:
                freq[source[i]] += 1

            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    res += 1

        return res