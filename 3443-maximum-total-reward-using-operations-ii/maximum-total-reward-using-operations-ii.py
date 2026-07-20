class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))

        dp = 1

        for value in rewardValues:
            dp |= (dp & ((1 << value) - 1)) << value

        return dp.bit_length() - 1