from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Define the get neighbors function
        def get_neighbors(position):
            new_x = [1, 2, 2, 1, -1, -2, -2, -1]
            new_y = [2, 1, -1, -2, -2, -1, 1, 2]
            moves = []
            for i in range(8):
                x = position[0] + new_x[i]
                y = position[1] + new_y[i]
                moves.append((x, y))
            return moves
        # Define the BFS function
        def bfs(x, y):
            # Define the queue list array
            queue = deque([(0, 0)])
            # Define the visited set
            visited = set()
            visited.add((0, 0))
            # Define the length as 0
            length = 0
            # while queue is not None
            while queue:
                # Do the regular level counting
                l = len(queue)
                for i in range(l):
                    n = queue.popleft()
                    if n == (x, y):
                        return length
                    for j in get_neighbors(n):
                        if j in visited:
                            continue
                        queue.append(j)
                        visited.add(j)
                length += 1
            
        return bfs(x, y)
