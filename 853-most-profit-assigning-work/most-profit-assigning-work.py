class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        cap_prof = defaultdict(int)
        merged = [[0,0] for _ in range(len(difficulty))]

        for i in range(len(profit)):
            merged[i] = [difficulty[i], profit[i]]

        merged.sort()
        difficulty.sort()

        max_till_now = merged[0][1] 

        for i in range(len(profit)):
            max_till_now = max(max_till_now, merged[i][1])
            cap_prof[merged[i][0]] = max_till_now

        result = 0
        
        for i in range(len(worker)):
            idx = bisect_right(difficulty, worker[i])
            if idx == 0:
                continue
            result += cap_prof[difficulty[idx - 1]]
        
        return result