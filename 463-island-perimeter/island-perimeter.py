class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        ans = 0

        def dfs(x, y):
            nonlocal ans

            vis[x][y] = True

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    ans += 1
                elif grid[nx][ny] == 0:
                    ans += 1
                elif not vis[nx][ny]:
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return ans