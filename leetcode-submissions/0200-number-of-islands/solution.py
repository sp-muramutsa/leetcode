from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Using DFS

        # Function too get the neighbors or possible moves of current position
        def get_neighbors(grid, position):
            length = len(grid[0])
            width = len(grid)
            possible_moves = []
            if position[0] - 1 >= 0:
                possible_moves.append((position[0]-1, position[1]))
            if position[0] + 1 < width:
                possible_moves.append((position[0]+1, position[1]))
            
            if position[1] - 1 >= 0:
                possible_moves.append((position[0], position[1]-1))

            if position[1] + 1 < length:
                possible_moves.append((position[0], position[1]+1))
            return possible_moves
        
        # BFS on the grid to find all number of islands
        def bfs(grid):
            queue = deque()
            visited = set()
            result = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == "0" or (i, j) in visited:
                        continue
                    queue.append((i, j))
                    while queue:
                        n = queue.popleft()
                        for (p, q) in get_neighbors(grid, (n[0], n[1])):
                            if grid[p][q] == "0" or (p, q) in visited:
                                continue
                            queue.append((p, q))
                            visited.add((p, q))

                    result += 1
            return result

        return bfs(grid)

