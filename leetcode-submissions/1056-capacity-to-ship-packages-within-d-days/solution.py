class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        n = len(weights)
        def can_ship(capacity: int) -> bool:
            i = 0

            for day in range(days):
                cap = capacity    
                while i < n and cap >= weights[i]:
                    cap -= weights[i]
                    i += 1      

            return i >= n
        
       
        
        # # [T, T, T, T, T, F] -> Return the first False

        # # 1 to total
        total = sum(weights)


        l, r = 0, total
        while l < r:
            mid = l + (r - l) // 2
            print(mid)
            if can_ship(mid):
                r = mid
            else:
                l = mid + 1
        
        return l

