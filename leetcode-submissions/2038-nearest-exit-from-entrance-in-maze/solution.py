from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if not maze:
            return -1

        rows, columns = len(maze), len(maze[0])

        visited = set()
        valid_exits = set()

        directions = ((1,0), (-1,0), (0,1), (0,-1))

        row, column = entrance[0], entrance[1]

        
        # def bfs(row, column):
        queue = deque([(row,column)])
        level = 0

        visited.add((row,column))

        while queue:
            step = len(queue)

            for i in range(step):
                r,c = queue.popleft()

                for direction_row, direction_column in directions:
                    current_row = r + direction_row
                    current_column = c + direction_column
                    if (
                        (current_row not in range(rows)) or
                        (current_column not in range(columns))
                    ):
                        distance = abs(r - row) + abs(c - column) 
                        if distance != 0:
                            return level
                            valid_exits.add(level)
                    elif (
                        (current_row in range(rows)) and
                        (current_column in range(columns)) and
                        (maze[current_row][current_column] == ".") and
                        ((current_row, current_column) not in visited)
                        ):
                        queue.append((current_row, current_column))
                        visited.add((current_row, current_column))
                        maze[current_row][current_column] = "+"
                
            level += 1


        return -1

