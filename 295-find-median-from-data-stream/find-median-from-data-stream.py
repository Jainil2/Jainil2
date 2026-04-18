class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []

    def _getlength(self):
        return [len(self.first), len(self.second)]

    def _balance(self):
        m, n = self._getlength()
        if abs(m - n) > 1:
            if m > n:
                t = heapq.heappop(self.first)
                heapq.heappush(self.second, -t)
            else:
                t = heapq.heappop(self.second)
                heapq.heappush(self.first, -t)

    def addNum(self, num: int) -> None:
        if self.second and num > self.second[0]:
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -num)
        self._balance()

    def findMedian(self) -> float:
        m, n = self._getlength()
        if (m + n) % 2:
            if m > n:
                return -self.first[0]
            else:
                return self.second[0]
        else:
            return (-self.first[0] + self.second[0]) / 2
        