class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Row reversal
        up, down = 0, n - 1
        while up < down:
            matrix[up], matrix[down] = matrix[down], matrix[up]
            up += 1
            down -= 1

        # Transpose
        row, col = -1, -1
        for _ in range(n):
            row += 1
            col += 1
            row_p, col_p = row + 1, col + 1
            while row_p < n and col_p < n:
                matrix[row][col_p], matrix[row_p][col] = (
                    matrix[row_p][col],
                    matrix[row][col_p],
                )
                row_p += 1
                col_p += 1

