class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)

            if ra == rb:
                return

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

        for u, v in edges:
            union(u, v)

        nodes = defaultdict(int)
        for i in range(n):
            nodes[find(i)] += 1

        edge_count = defaultdict(int)
        for u, v in edges:
            edge_count[find(u)] += 1

        ans = 0

        for root in nodes:
            k = nodes[root]
            required = k * (k - 1) // 2

            if edge_count[root] == required:
                ans += 1

        return ans