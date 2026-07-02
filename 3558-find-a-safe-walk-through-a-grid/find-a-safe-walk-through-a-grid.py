class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        h = []
        dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        vis = [[-1] * n for _ in range(m)]
        if grid[0][0] == 1:
            heapq.heappush(h, (-health + 1, 0, 0))
            vis[0][0] = health - 1
        else:
            heapq.heappush(h, (-health, 0, 0))
            vis[0][0] = health
        while h:
            health, x, y = heapq.heappop(h)
            if x == m - 1 and y == n - 1 and health < 0:
                return True
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    next_health = None
                    if grid[nx][ny] == 1:
                        next_health = -health - 1
                    else:
                        next_health = -health
                    if next_health > vis[nx][ny]:
                        vis[nx][ny] = next_health
                        heapq.heappush(h, (-next_health, nx, ny))
        return False
