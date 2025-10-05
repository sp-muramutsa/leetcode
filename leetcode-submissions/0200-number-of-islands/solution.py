from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if len(grid) == 0:
            return 0

        rows, columns = len(grid), len(grid[0])
        seen = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        answer = 0

        def bfs(row, column):
            seen.add((row,column))
            queue = deque()
            queue.append((row,column))
            
            while queue:
                r, c = queue.popleft()

                for x, y in directions:
                    current_row = r + x
                    current_column = c + y

                    if ( (current_row in range(rows)) and
                         (current_column in range(columns)) and
                         ((current_row,current_column) not in seen) and
                         ( grid[current_row][current_column] == "1")
                        ):
                        seen.add((current_row,current_column))
                        queue.append((current_row,current_column))


        for row in range(rows):
            for column in range(columns):

                if (((row,column) not in seen) and (grid[row][column] == "1")):
                    bfs(row,column)
                    answer += 1

        return answer
