from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Make it a set
        s = set(candyType)
        # Get the max number of candies
        maximum_candies = len(candyType) / 2
        # If the length of the set is grater than the maximum number return the maximum number
        if len(s) >= maximum_candies:
            return int(maximum_candies)
        # Else return the number of the set
        return int(len(s))
