class Solution:
    def can_repair(self, time, ranks, total_cars):
        repaired_cars = 0
        for r in ranks:
            repaired_cars += floor(sqrt(time / r))

        return repaired_cars >= total_cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, max(ranks) * (cars ** 2)

        while l < r:
            mid = l + (r - l) // 2

            if self.can_repair(mid, ranks, cars):
                r = mid
            else:
                l = mid + 1
        
        return l

