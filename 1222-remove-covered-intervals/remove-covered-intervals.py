class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[0] ,-x[1]))
        print(intervals)
        start, end = intervals[0][0], intervals[0][1]
        res = 1
        for i in range(1, len(intervals)):
            if start <= intervals[i][0] and intervals[i][1] <= end:
                continue
            else:
                res += 1
                start, end = intervals[i][0], intervals[i][1] 
        return res