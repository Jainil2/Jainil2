class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        max_val = max(costs)
    
        count = [0] * (max_val + 1)
        output = [0] * len(costs)
        
        for num in costs:
            count[num] += 1
            
        for i in range(1, len(count)):
            count[i] += count[i - 1]
            
        for num in reversed(costs):
            output[count[num] - 1] = num
            count[num] -= 1

        result, sum = 0, 0
        for cost in output:
            if sum + cost > coins:
                return result
            sum += cost
            result += 1
        return result