class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Intuition: Put two dummy zeroes at the start and the end of the array. Then iterate while checking if an index is viable for flower planting. Count the viable indexes and compare them to n. Remember to skip 2 places when you find a viable index.
        """
        length = len(flowerbed) + 1 
        flowerbed = [0] + flowerbed + [0]
        k = 0
        i = 1
        while i < length:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                k += 1
                i += 1
            i += 1
        return k >= n




       

        

        
