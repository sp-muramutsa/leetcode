class Solution:
    def isHappy(self, n: int) -> bool:
        # Create a set the keeps visited numbers
        visited = set()
        # Implement a function that calculates the sum
        def tot(num):
            res = 0
            while num >= 10:
                res += (num%10)**2
                num = num // 10
            res += (num)**2
            print(res)
            return res
        
        # While sum is not in visited
        while n not in visited:
            # Store n in visited
            visited.add(n)
            total = tot(n)
            # If sum is 1 returnn True
            if total == 1:
                return True
            n = total
        # Return False
        return False
