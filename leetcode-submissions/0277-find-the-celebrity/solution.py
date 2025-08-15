# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:

        can_be = {i: True for i in range(n)}

        for i in range(n):
            for j in range(n):

                if i == j:
                    continue
                    
                if not can_be[j]:
                    continue
                
                if knows(i, j):
                    can_be[i] = False
                else:
                    can_be[j] = False

                if knows(j, i):
                    can_be[j] = False
                else:
                    can_be[i] = False

        for k in range(n):
            if can_be[k]:
                return k

        return -1

