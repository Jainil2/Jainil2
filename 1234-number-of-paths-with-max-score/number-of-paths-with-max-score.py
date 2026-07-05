class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        dirs = [(-1, 0), (0, -1), (-1, -1)]
        memo = {}

        def dfs(x, y):
            if x < 0 or y < 0 or board[x][y] == 'X':
                return (-1, 0)

            if x == 0 and y == 0:
                return (0, 1)

            if (x, y) in memo:
                return memo[(x, y)]

            best_score = -1
            ways = 0

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                score, cnt = dfs(nx, ny)

                if score == -1:
                    continue

                if score > best_score:
                    best_score = score
                    ways = cnt
                elif score == best_score:
                    ways = (ways + cnt) % MOD

            if best_score == -1:
                memo[(x, y)] = (-1, 0)
                return memo[(x, y)]

            cur = 0 if board[x][y] in "SE" else int(board[x][y])

            memo[(x, y)] = (best_score + cur, ways % MOD)
            return memo[(x, y)]

        score, ways = dfs(n - 1, n - 1)

        if score == -1:
            return [0, 0]

        return [score, ways]