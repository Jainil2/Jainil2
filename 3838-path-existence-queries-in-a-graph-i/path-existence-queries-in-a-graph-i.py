class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return
        
        if self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        elif self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.rank[ra] += 1
            self.parent[rb] = ra
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        uf = UnionFind(n)

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                uf.union(i, i - 1)
        
        result = []

        for u, v in queries:
            result.append(uf.connected(u, v))
        
        return result

        