from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the cells tha are adjacent to the Pacific
        adj_pacific_cells = []
        for j in range(len(heights[0])):
            adj_pacific_cells.append((0, j))

        for i in range(len(heights)):
            adj_pacific_cells.append((i, 0))
        # Get the cells that area adjacent to the atlantic
        adj_atlantic_cells = []
        for j in range(len(heights[0])):
            adj_atlantic_cells.append((len(heights)-1, j))

        for i in range(len(heights)):
            adj_atlantic_cells.append((i, len(heights[0])-1))

        def get_neighbors(cell, grid):
            new_r = [1, 0, -1, 0]
            new_c = [0, 1, 0, -1]
            moves = []

            for i in range(4):
                r = new_r[i] + cell[0]
                c = new_c[i] + cell[1]

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] >= grid[cell[0]][cell[1]]:
                    moves.append((r, c))

            return moves
        # Us bfs to get the cells where cells have a greater height
        def bfs(grid, adj):
            visited = set()
            queue = deque()
            for i in adj:
                visited.add(i)
                queue.append(i)
            while queue:
                n = queue.popleft()
                for cell in get_neighbors(n, grid):
                    if cell in visited:
                        continue

                    visited.add(cell)
                    queue.append(cell)
            return visited

        # Add those cells to Pacific list
        res_pacific = bfs(heights, adj_pacific_cells)
        # Do the same for those in Atlantic list
        res_atlantic = bfs(heights, adj_atlantic_cells)

        # Return the intersection
        return list(res_pacific & res_atlantic)
