class Solution:
    def can_eat_all(self, rate: int, h: int, piles: List[int]) -> bool:      
        hours = 0
        for pile in piles:
            hours += ceil(pile / rate)
        return hours <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        while l < r:
            rate = l + (r - l) // 2  
            if self.can_eat_all(rate, h, piles):
                r = rate
            else:
                l = rate + 1
        
        return l
