class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        ROWS, COLS = len(mat), len(mat[0])
        total_cells = ROWS * COLS
        visited_cells = 0
        path = []
        row, col = 0, 0
        col_start = 0
        i = 0

        while True:

            row = min(i, ROWS - 1)
            if i < ROWS:
                col = 0
            else:
                col_start += 1
                col = col_start

            diag = []
            while row > -1 and col < COLS:
                diag.append(mat[row][col])
                visited_cells += 1
                row -= 1
                col += 1

                if visited_cells >= total_cells:
                    continue

            if i % 2 == 1:
                diag = diag[::-1]
            path.extend(diag)
            i += 1

            if visited_cells >= total_cells:
                break

        return path

    

