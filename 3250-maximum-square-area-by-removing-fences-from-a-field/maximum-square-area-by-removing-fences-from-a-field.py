class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = sorted(hFences + [1, m])
        vFences = sorted(vFences + [1, n])
        
        def get_gaps(fences):
            gaps = set()
            for i in range(len(fences)):
                for j in range(i + 1, len(fences)):
                    gaps.add(fences[j] - fences[i])
            return gaps

        h_gaps = get_gaps(hFences)
        v_gaps = get_gaps(vFences)
        
        common_gaps = h_gaps.intersection(v_gaps)
        
        if not common_gaps:
            return -1
        
        max_side = max(common_gaps)
        return (max_side * max_side) % 1_000_000_007