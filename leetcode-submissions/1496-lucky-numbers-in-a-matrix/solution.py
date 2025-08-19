class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        ROWS, COLS = len(matrix), len(matrix[0])

        r_min_maximum = float("-inf")
        for row in range(ROWS):
            min_row = min(matrix[row])
            r_min_maximum = max(r_min_maximum, min_row)

        c_max_minimum = float("inf")
        for col in range(COLS):
            max_col = max(matrix[r][col] for r in range(ROWS))
            c_max_minimum = min(c_max_minimum, max_col)

        if r_min_maximum == c_max_minimum:
            return [c_max_minimum]
        return []

