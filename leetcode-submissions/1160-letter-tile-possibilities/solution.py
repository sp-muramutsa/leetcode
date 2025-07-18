class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        solution = 0
        tiles = list(tiles)
        tiles.sort()
        n = len(tiles)
        used = {i: False for i in range(n)}

        def backtrack(i, path_len, used):

            nonlocal solution
            solution += 1

            if path_len == n:
                return

            for j in range(n):

                if j > 0 and tiles[j] == tiles[j - 1] and not used[j - 1]:
                    continue

                if used[j]:
                    continue

                used[j] = True
                backtrack(j + 1, path_len + 1, used)
                used[j] = False

        backtrack(0, 0, used)
        return solution - 1

