class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Time O(n)
        Space O(1)
        """

        # we should iterate while planting. isolate case: first index and last ind
        plant = 0
        length = len(flowerbed)

        
        for i in range(length):
            neighbors = []
            if i - 1 > -1:
                neighbors.append(flowerbed[i - 1])
            if i + 1 < length:
                neighbors.append(flowerbed[i + 1])

            if flowerbed[i] == 0 and 1 not in neighbors: # plant a flower if space is empty
                flowerbed[i] = 1
                plant += 1
                i += 1
            
        if plant >= n:
            return True
        else:
            return False


        

        
