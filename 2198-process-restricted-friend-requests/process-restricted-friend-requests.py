class UnionFind:
    def __init__(self, n, res):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.res = res
        self.friend = defaultdict(list)
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        findu = self.find(u)
        findv = self.find(v)

        if findu == findv:
            return True
        
        for a, b in self.res:
            ra = self.find(a)
            rb = self.find(b)
            if (ra == findu and rb == findv) or (ra == findv and rb == findu):
                return False
        
        if self.rank[findu] < self.rank[findv]:
            self.parent[findu] = findv
        elif self.rank[findv] < self.rank[findu]:
            self.parent[findv] = findu
        else:
            self.parent[findv] = findu
            self.rank[findu] += 1

        return True
    
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        result = []
        
        uf = UnionFind(n, restrictions)
        
        for u, v in requests:
            if uf.union(u, v):
                result.append(True)
            else:
                result.append(False)
        
        return result
        