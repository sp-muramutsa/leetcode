class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Identify the get neighbors function
        def get_neighbors(position, grid):
            col_move = [0, 1, 0, -1]
            row_move = [1, 0, -1, 0]
            moves = []
            for i in range(4):
                new_col = position[1] + col_move[i]
                new_row = position[0] + row_move[i]
                if 0 <= new_col and new_col < len(grid[0]) and 0 <= new_row and new_row < len(grid) and grid[new_row][new_col] == grid[position[0]][position[1]]:
                    moves.append((new_row, new_col))
            return moves

        # Define the dfs function
        def dfs(grid, sr, sc, color):
            # Identify the visited set
            visited = set()
            visited.add((sr, sc))
            # Create a stack
            stack = [] 
            # Add the starting pixel to the stack
            stack.append((sr, sc))
            # While stack is not empty
            while stack:
                # Pop from the stack
                n = stack.pop()
                # Get the positions neighbors
                for i in get_neighbors(n, grid):
                    # If the neighbor is in visited skip
                    if i in visited:
                        continue
                    # Add the neighbor to the stack 
                    stack.append(i)
                    # Add the current position to the visited data structure
                    visited.add(i)
                grid[n[0]][n[1]] = color
            # Return the  modified grid
            return grid

        return dfs(image, sr, sc, color)
