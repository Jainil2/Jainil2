class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60 
       
        def cost(mm, ss):
            print(mm, ss)
            arr = [mm // 10, mm % 10, ss // 10, ss % 10]
            print(arr)
            cur, result = startAt, 0
            i = 0
            while i < 4 and arr[i] == 0:
                i += 1
            while i < 4:
                if arr[i] == cur:
                    result += pushCost
                else:
                    result += pushCost + moveCost
                    cur = arr[i]
                i += 1
            print(result)
            return result
        if minutes > 99:
            return cost(minutes - 1, seconds + 60)
        if seconds + 60 <= 99:
            return min(cost(minutes, seconds), cost(minutes - 1, seconds + 60))
        return cost(minutes, seconds)