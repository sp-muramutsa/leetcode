class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # Multi-source shortest path bfs. Start from the gate. Move inwards into the rooms.
        m, n = len(rooms), len(rooms[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((0, r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:

            dist, row, col = q.popleft()

            for dx, dy in directions:
                x, y = row + dx, col + dy
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                    rooms[x][y] = dist + 1
                    q.append((dist + 1, x, y))

