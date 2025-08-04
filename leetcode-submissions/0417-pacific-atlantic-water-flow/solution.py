class Solution:
    def dfs(self, cell: tuple, heights: List[List[int]], visited: set) -> set:

        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(cell):

            visited.add(cell)
            row, col = cell

            for dx, dy in movements:
                x, y = row + dx, col + dy
                if (
                    0 <= x < ROWS
                    and 0 <= y < COLS
                    and (x, y) not in visited
                    and heights[row][col] <= heights[x][y]
                ):

                    dfs((x, y))

        dfs(cell)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])

        # Pacific Ocean
        pacific_visited = set()
        for i in range(COLS):
            self.dfs((0, i), heights, pacific_visited)

        for j in range(ROWS):
            self.dfs((j, 0), heights, pacific_visited)

        print(pacific_visited)

        # Atlantic ocean
        atlantic_visited = set()
        for k in range(COLS):
            self.dfs((ROWS - 1, k), heights, atlantic_visited)

        for l in range(ROWS):
            self.dfs((l, COLS - 1), heights, atlantic_visited)

        print(atlantic_visited)

        return list(pacific_visited.intersection(atlantic_visited))

