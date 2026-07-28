class Solution:
    def smallestPalindrome(self, s: str) -> str:
        res = ""
        last = None
        freq = Counter(s)
        for i in range(97, 123):
            t = chr(i)
            if freq[t] % 2:
                last = t
            if t in freq:
                res += t * (freq[t] // 2)
        temp = res[::-1]
        if last:
            res += last
        result = res + temp
        return result 