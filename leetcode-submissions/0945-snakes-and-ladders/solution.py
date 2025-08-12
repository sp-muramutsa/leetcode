class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        adj = []
        n_squared = n**2
        number = 1

        reverse = False
        for i in range(n):
            row = []
            for j in range(n):
                row.append(number)
                number += 1

            if reverse:
                row = row[::-1]

            reverse = not reverse
            adj.append(row)

        adj = list(reversed(adj))
        hashmap = {adj[row][col]: (row, col) for row in range(n) for col in range(n)}
        q = deque([(0, 1)])
        visited = set([1])

        while q:

            rolls, curr = q.popleft()

            # Goal
            if curr == n_squared:
                return rolls

            start, end = curr + 1, min(curr + 6, n_squared)

            for dest in range(start, end + 1):

                nr, nc = hashmap[dest]

                if board[nr][nc] != -1:
                    dest = board[nr][nc]

                if dest in visited:
                    continue

                visited.add(dest)
                q.append((rolls + 1, dest))

        return -1

