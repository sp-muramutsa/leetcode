class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Get the positions with 0
        # Keep the positions in a set
        # Iterate over the matrix and if position in set change the row and column

        s = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    s.add((i, j))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) in s:
                    for r in range(len(matrix)):
                        matrix[r][j] = 0
                    for c in range(len(matrix[0])):
                        matrix[i][c] = 0

        return matrix
