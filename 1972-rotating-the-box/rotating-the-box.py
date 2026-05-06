class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        for row in range(m):
            cur, move = n - 1, n - 1
            while cur >= 0:
                if boxGrid[row][cur] == '*':
                    move = cur - 1
                elif boxGrid[row][cur] == '#':
                    boxGrid[row][cur] = '.'
                    boxGrid[row][move] = '#'
                    move -= 1
                cur -= 1
        result = [[None] * m for _ in range(n)]
        for j in range(n):
            k = 0
            for i in range(m - 1, -1, -1):
                result[j][k] = boxGrid[i][j]
                k += 1
        return result