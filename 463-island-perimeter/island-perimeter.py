class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = [0]
        m, n = len(grid), len(grid[0])
        dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        vis = [[False] * n for _ in range(m)]
        def dfs(x, y, result):
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not vis[nx][ny]:
                    vis[nx][ny] = True
                    dfs(nx, ny, result)
                elif (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and not vis[nx][ny]):
                    result[0] += 1
                elif nx >= m or nx < 0 or ny >= n or ny < 0:
                    result[0] += 1
        f = False
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    vis[i][j] = True
                    dfs(i, j, result)
                    f = True
                    break
            if f:
                break
                    
        return result[0]
