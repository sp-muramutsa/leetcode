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

        solution = []
        k = len(digits)
        if k == 0:
            return []

        def backtrack(i, path):
            if i == k:
                solution.append("".join(path))
                return

            for char in hashmap[digits[i]]:
                path.append(char)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return solution

