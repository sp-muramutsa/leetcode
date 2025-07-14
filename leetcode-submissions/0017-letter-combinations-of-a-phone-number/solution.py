class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hashmap = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        solution, path = [], []

        chars = [char for char in digits]

        n = len(chars)
        k = len(digits)

        def get_neighbors(idx):
            neighbors = set()
            for j in range(idx + 1, n):
                for char in hashmap[chars[j]]:
                    neighbors.add((j, char))

            return neighbors

        def backtrack(i):
            if len(path) == k and path:
                solution.append("".join(path))
                return

            if i == n:
                return

            for neighbor in get_neighbors(i):
                idx, char = neighbor
                path.append(char)
                backtrack(idx)
                path.pop()

        backtrack(-1)
        return solution

