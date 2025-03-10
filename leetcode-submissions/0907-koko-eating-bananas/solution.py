class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = 1, max(piles)

        while minRate < maxRate:
            midRate = minRate + (maxRate - minRate) // 2
        
            time = 0
            for pile in piles:
                time += math.ceil(pile / midRate) # Take ceiling bc Koko will not eat more bananas during this our (read quesiton carefullt)
            
            # Unworkable: we need to increase the rate
            if time > h:
                minRate = midRate + 1
            
            # Workable: we need to reduce the rate. But cautiously since midRate is valid too! And thus, it might be the first valid value
            else:
                maxRate = midRate
            
        return minRate
        
                

        
