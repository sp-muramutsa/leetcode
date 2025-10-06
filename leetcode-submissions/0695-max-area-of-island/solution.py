from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        visited = set()
        answer = 0
        
        rows, columns = len(grid), len(grid[0])
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(row,column):
            visited.add((row,column))
            area = 0
            queue = deque([(row,column)])
            
            while queue:
                r, c = queue.popleft()
                area += 1
                
                for direction_row, direction_column in directions:
                    current_row = r + direction_row
                    current_column = c + direction_column
                    
                    if  (
                        (current_row in range(rows)) and
                        (current_column in range(columns)) and
                        (grid[current_row][current_column] == 1) and
                        ((current_row,current_column) not in visited)
                        ):
                        visited.add((current_row,current_column))
                        queue.append((current_row,current_column))
                        
            return area
                
        for row in range(rows):
            for column in range(columns):
                if((row, column) not in visited) and (grid[row][column] == 1):
                    answer = max(answer,bfs(row,column))
                    
        return answer
