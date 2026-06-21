class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * (max(costs) + 1)

        for cost in costs:
            freq[cost] += 1

        ans = 0

        for cost, count in enumerate(freq):
            if count == 0:
                continue

            can_buy = min(count, coins // cost)
            ans += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return ans