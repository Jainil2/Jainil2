class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = Counter()
        mid = ""

        for ch in sorted(freq):
            half[ch] = freq[ch] // 2
            if freq[ch] & 1:
                mid = ch

        LIMIT = k

        def count_perm(cnt):
            total = sum(cnt.values())
            ans = 1

            for x in cnt.values():
                if x == 0:
                    continue
                ans *= comb(total, x)
                if ans > LIMIT:
                    return LIMIT + 1
                total -= x

            return ans

        if count_perm(half) < k:
            return ""

        first = []

        while sum(half.values()) > 0:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_perm(half)

                if ways >= k:
                    first.append(ch)
                    break

                k -= ways
                half[ch] += 1

        first = "".join(first)
        return first + mid + first[::-1]