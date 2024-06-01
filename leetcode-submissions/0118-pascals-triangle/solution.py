class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        """
        Intuition: Put 2 dummy zeros on either side of the previous array
        Time: O(n^2)
        Space: O(n^2)
        """

        triangle = [[1]]
        
        for i in range(1, numRows):
            previous = [0] + triangle[i-1] + [0] # dummy zeros on either side
            level = []

            for j in range(i + 1):
                level.append(previous[j] + previous[j+1])
            triangle.append(level)
            
        return triangle

