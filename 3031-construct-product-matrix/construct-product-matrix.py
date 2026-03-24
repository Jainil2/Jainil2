class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j] % MOD)
        
        size = m * n
        
        pref = [1] * size
        suff = [1] * size
        
        for i in range(1, size):
            pref[i] = (pref[i-1] * arr[i-1]) % MOD
        
        for i in range(size - 2, -1, -1):
            suff[i] = (suff[i+1] * arr[i+1]) % MOD
        
        res = [[0] * n for _ in range(m)]
        
        for idx in range(size):
            val = (pref[idx] * suff[idx]) % MOD
            i, j = divmod(idx, n)
            res[i][j] = val
        
        return res