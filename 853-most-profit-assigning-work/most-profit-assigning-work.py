from bisect import bisect_right

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        
        max_profit = 0
        diffs = []
        profits = []
        
        for d, p in jobs:
            max_profit = max(max_profit, p)
            diffs.append(d)
            profits.append(max_profit)
        
        result = 0
        for w in worker:
            idx = bisect_right(diffs, w) - 1
            if idx >= 0:
                result += profits[idx]
        
        return result