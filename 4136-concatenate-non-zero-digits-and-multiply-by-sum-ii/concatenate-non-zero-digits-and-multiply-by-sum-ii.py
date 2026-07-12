class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        n = len(s)

        digit_sum = [0] * (n + 1)
        nonzero_cnt = [0] * (n + 1)
        prefix_num = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)

            digit_sum[i + 1] = digit_sum[i] + d
            nonzero_cnt[i + 1] = nonzero_cnt[i] + (d != 0)

            if d != 0:
                prefix_num[i + 1] = (prefix_num[i] * 10 + d) % MOD
            else:
                prefix_num[i + 1] = prefix_num[i]

        max_nonzero = nonzero_cnt[n]

        pow10 = [1] * (max_nonzero + 1)
        for i in range(1, max_nonzero + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []

        for l, r in queries:
            r += 1

            length = nonzero_cnt[r] - nonzero_cnt[l]

            x = (
                prefix_num[r]
                - prefix_num[l] * pow10[length]
            ) % MOD

            ssum = digit_sum[r] - digit_sum[l]

            ans.append((x * ssum) % MOD)

        return ans