class Solution:
    def check(self, grid, x, y, px, py, vis, m, n):
        vis[x][y] = True
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                # Only consider same character
                if grid[nx][ny] != grid[x][y]:
                    continue

                # Skip parent
                if nx == px and ny == py:
                    continue

                # If already visited → cycle
                if vis[nx][ny]:
                    return True

                # Continue DFS
                if self.check(grid, nx, ny, x, y, vis, m, n):
                    return True

        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        vis = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    if self.check(grid, i, j, -1, -1, vis, m, n):
                        return True

        return False