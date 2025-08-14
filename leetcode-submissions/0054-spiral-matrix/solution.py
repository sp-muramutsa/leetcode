class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ROWS, COLS = len(matrix), len(matrix[0])
        path = []

        left_lim = -1
        right_lim = COLS
        up_lim = 0
        down_lim = ROWS
        visited = 0
        cells = ROWS * COLS

        while True:

            # Go right
            row = up_lim
            for col in range(left_lim + 1, right_lim):
                path.append(matrix[row][col])
                visited += 1
            right_lim -= 1

            if visited == cells:
                break

            # Go down
            col = right_lim
            for row in range(up_lim + 1, down_lim):
                path.append(matrix[row][col])
                visited += 1
            down_lim -= 1

            if visited == cells:
                break

            # Go left
            row = down_lim
            for col in range(right_lim - 1, left_lim, -1):
                path.append(matrix[row][col])
                visited += 1
            left_lim += 1

            if visited == cells:
                break

            # Go up
            col = left_lim
            for row in range(down_lim - 1, up_lim, -1):
                path.append(matrix[row][col])
                visited += 1
            up_lim += 1

            if visited == cells:
                break

        return path

