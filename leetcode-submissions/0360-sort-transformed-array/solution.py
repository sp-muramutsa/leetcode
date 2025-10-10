class Solution:
    def sortTransformedArray(
        self, nums: List[int], a: int, b: int, c: int
    ) -> List[int]:
        """
        # Quadratic function
        # O(nlogn)

        # O(n) ?

        # Find the roots?
        # x^2 + 3x + 5
        # b ** 2 - 4ac = 9 - 4(5)  = -16

        # Vertex
        - -b/2a
        - -3/2
        - f(-3,2) = 9/4 + (-9/2) + 5 = (9 - 18 + 20) / 4 = 11 / 4
        - (-3/2, 11/ 4)

        - 9, 3, 15, 33
        - 2.75

        - Parity?
        - sign of a

        - parity here is positive
        - so: decrease, then we hit 0 (vertex), then increase

        - Find the point of increase: 3 to 15 here. Then in sorting we do it like this:
            - pick two points close to the center and pick the small one
            - move the pointer in the direction of the one you picked
            - keep going again and again till done
            - buenaaa
        """

        def quadratic(x):
            return (a * (x**2)) + (b * x) + c

        y_values = [quadratic(x) for x in nums]
        print(y_values)

        n = len(y_values)

        result = []
        l, r = 0, n - 1

        if a < 0:
            while l <= r:
                if y_values[l] < y_values[r]:
                    result.append(y_values[l])
                    l += 1
                else:
                    result.append(y_values[r])
                    r -= 1
            return result
            
        else:
            while l <= r:
                if y_values[l] < y_values[r]:
                    result.append(y_values[r])
                    r -= 1
                else:
                    result.append(y_values[l])
                    l += 1
        
            return result[::-1]
        


