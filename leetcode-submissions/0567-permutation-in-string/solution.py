from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        counter_1 = {chr(i + ord("a")): 0 for i in range(26)}
        counter_2 = {chr(i + ord("a")): 0 for i in range(26)}

        for char in s1:
            counter_1[char] += 1

        for char in s2[:k]:
            counter_2[char] += 1

        # First window: O(26)
        matches = 0
        for key in counter_1:
            if counter_1[key] == counter_2[key]:
                matches += 1

        n = len(s2)
        l, r = 0, k

        # Main loop

        while r < n:
            
            if matches == 26:
                return True
        
            if counter_2[s2[l]] == counter_1[s2[l]]:
                matches -= 1

            if counter_2[s2[r]] == counter_1[s2[r]]:
                matches -= 1

            counter_2[s2[l]] -= 1
            counter_2[s2[r]] += 1

            if counter_2[s2[l]] == counter_1[s2[l]]:
                matches += 1

            if counter_2[s2[r]] == counter_1[s2[r]]:
                matches += 1

            l += 1
            r += 1       
      
        return matches == 26

