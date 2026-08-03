class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            curr = 0
            curr_max = float('-inf')
            for k in range(1, 4):
                if i + k - 1 < n:
                    curr += stoneValue[i + k - 1]
                    opp = dp[i + k]
                    diff = curr - opp
                    curr_max = max(curr_max, diff)
            dp[i] = curr_max
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
        