class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def rotations(x):
            top_rot = bottom_rot = 0
            for t, b in zip(tops, bottoms):
                if t != x and b != x:
                    return float('inf')
                if t != x:
                    top_rot += 1
                if b != x:
                    bottom_rot += 1
            return min(top_rot, bottom_rot)

        res = min(rotations(tops[0]), rotations(bottoms[0]))
        return res if res != float('inf') else -1
