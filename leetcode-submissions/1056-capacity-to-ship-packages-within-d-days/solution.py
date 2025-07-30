class Solution:
    def can_ship(self, capacity, weights, count, actual_days):

        days = 0
        i = 0
        while i < count:
            # Ship for a day depending on capacity
            curr_capacity = capacity
            while curr_capacity > 0 and i < count:
                if curr_capacity < weights[i]:
                    break
                else:
                    curr_capacity -= weights[i]
                    i += 1
            days += 1

            if days > actual_days:
                return False

        return days <= actual_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        n = len(weights)
        l, r = 1, sum(weights) 

        while l < r:
            mid = l + (r - l) // 2
            if self.can_ship(mid, weights, n, days):
                r = mid
            else:
                l = mid + 1

        return l

