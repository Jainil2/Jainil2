class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count, sum = 0, 0
        for cost in costs:
            if sum + cost > coins:
                return count
            sum += cost
            count += 1
        return count