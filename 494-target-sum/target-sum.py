class Solution:
    def track(self, nums, i, cur, target, n, dp, total):
        if i == n:
            return 1 if cur == target else 0
        
        if dp[i][cur + total] != -1:
            return dp[i][cur + total]
        
        dp[i][cur + total] = (
            self.track(nums, i + 1, cur + nums[i], target, n, dp, total) +
            self.track(nums, i + 1, cur - nums[i], target, n, dp, total)
        )
        
        return dp[i][cur + total]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        dp = [[-1] * (2 * total + 1) for _ in range(n)]
        
        return self.track(nums, 0, 0, target, n, dp, total)