class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        n = len(people)
        l, r = 0, n - 1

        people.sort()
        boats = 0

        while l <= r:
            if people[r] + people[l] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            boats += 1

        return boats

