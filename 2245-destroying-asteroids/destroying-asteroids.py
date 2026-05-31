class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        while asteroids:
            idx = bisect.bisect_right(asteroids, mass) - 1
            if idx >= 0 and asteroids[idx] <= mass:
                mass += asteroids[idx]
            else:
                break
            del asteroids[idx]
        return len(asteroids) == 0
