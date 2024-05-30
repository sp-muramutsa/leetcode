# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        """
        Binary search
        Time: O(logn)
        Space: O(1)
        Intuition: Just like the guessing game, we eliminate a number we     guessed along with either all the numbers greater than it or less.
        """
        l, r = 0, n

        while l <= r:
            mid = l + (r - l) // 2
            guessed = guess(mid)
            print(mid, guessed)
            if guessed == -1:
                r = mid - 1 
            elif guessed == 1:
                l = mid + 1
            elif guessed == 0:
                return mid
    
