from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # BFS
        # Start with a QueueFrontier with all rotten oranges
        # Initialize minutes = 0
        # While the frontier is not empty
        # For each cell in the frontier
        # Add its neighbors to the frontiner
        # Update minutes by 1
        # If all cells are rotten, return minutes. Else return -1.

        # Edge cases
        # No fresh oranges initially: 0
        # No rotten ones to begin with: -1

        n = len(grid)
        m = len(grid[0])
        frontier = []
        explored = set()

        fresh_count, rotten_count = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    frontier.append((i, j))

                if grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        def get_fresh_neighbors(cell: tuple) -> List:

            i, j = cell
            neighbors = set()

            # Vertical
            for x in range(i - 1, i + 2, 2):
                if x >= 0 and x < n:
                    if grid[x][j] == 1:
                        neighbors.add((x, j))

            # Horizontal
            for y in range(j - 1, j + 2, 2):
                if y >= 0 and y < m:
                    if grid[i][y] == 1:
                        neighbors.add((i, y))

            return neighbors

        minutes = 0
        while frontier:
            print(frontier, minutes)
            minutes += 1
            for cell in frontier.copy():

                # Mark the cell as rotten
                i, j = cell
                frontier.remove(cell)
                explored.add(cell)
                grid[i][j] = 2

                neighbors = get_fresh_neighbors(cell)

                for neighbor in neighbors:
                    if neighbor not in frontier and neighbor not in explored:
                        frontier.append(neighbor)

        # Check if all oranges are rotten
        no_fresh = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    no_fresh = False

        return minutes - 1 if no_fresh else -1

