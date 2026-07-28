class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.max_size = 1
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return
        
        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u
            
        self.parent[root_v] = root_u
        self.size[root_u] += self.size[root_v]
        self.max_size = max(self.max_size, self.size[root_u])

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        uf = UnionFind(max_num)
        
        factor_to_num = {}
        
        for num in nums:
            current = num
            d = 2
            while d * d <= current:
                if current % d == 0:
                    if d in factor_to_num:
                        uf.union(num, factor_to_num[d])
                    else:
                        factor_to_num[d] = num
                    while current % d == 0:
                        current //= d
                d += 1
            if current > 1:
                if current in factor_to_num:
                    uf.union(num, factor_to_num[current])
                else:
                    factor_to_num[current] = num
                    
        return uf.max_size
