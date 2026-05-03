class Solution:
    def solve(self, board, row, col, box, x, y):
        if x == 9:
            return True
        if y == 9:
            return self.solve(board, row, col, box, x + 1, 0)
        if board[x][y] != ".":
            return self.solve(board, row, col, box, x, y + 1)
            
        idx = 3 * (x // 3) + y // 3

        for i in range(1, 10):
            if i not in row[x] and i not in col[y] and i not in box[idx]:
                board[x][y] = str(i)
                box[idx].add(i)
                row[x].add(i)
                col[y].add(i)
                if self.solve(board, row, col, box, x, y + 1):
                    return True
                board[x][y] = "."
                box[idx].remove(i)
                row[x].remove(i)
                col[y].remove(i)

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                idx = 3 * (i // 3) + j // 3
                if board[i][j] != ".":
                    val = int(board[i][j])
                    row[i].add(val)
                    col[j].add(val)
                    box[idx].add(val)
        
        self.solve(board, row, col, box, 0, 0)
        
