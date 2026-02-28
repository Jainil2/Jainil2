class Solution:
    def __init__(self):
        self.MAXN = 100001
        self.isPrime = [True] * self.MAXN
        self.sieve()
    
    def sieve(self):
        self.isPrime[0] = self.isPrime[1] = False
        for i in range(2, int(self.MAXN ** 0.5) + 1):
            if self.isPrime[i]:
                for j in range(i * i, self.MAXN, i):
                    self.isPrime[j] = False

    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        res = 0
        prev = -1
        curr = -1
        
        ms = []
        
        for r in range(n):
            
            if nums[r] < self.MAXN and self.isPrime[nums[r]]:
                prev = curr
                curr = r
                bisect.insort(ms, nums[r])
            
            while ms and (ms[-1] - ms[0] > k):
                if nums[l] < self.MAXN and self.isPrime[nums[l]]:
                    idx = bisect.bisect_left(ms, nums[l])
                    ms.pop(idx)
                l += 1
            
            if len(ms) >= 2:
                res += (prev - l + 1)
        
        return res