class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_counts = [0] * (n + 1)  # Initialize trust counts for each person
        
        for a, b in trust:
            trust_counts[a] -= 1  # Decrease trust count for person a
            trust_counts[b] += 1  # Increase trust count for person b

        for i in range(1, n + 1):
            if trust_counts[i] == n - 1:  # Check if person i is trusted by everyone except themselves
                return i

        return -1  # No judge found

            
        
        
        
