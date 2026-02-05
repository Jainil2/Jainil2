class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        idx = defaultdict(set)
        freq = defaultdict(int)
        freq2 = defaultdict(int)
        n = len(tops)
        for i in range(n):
            idx[tops[i]].add(i)
            freq[tops[i]] += 1
        for i in range(n):
            idx[bottoms[i]].add(i)
            freq2[bottoms[i]] += 1
        for i, _ in idx.items():
            if len(idx[i]) == len(tops):
                return min(freq[i], min(n - freq[i], min(n - freq2[i], freq2[i])))
        return -1