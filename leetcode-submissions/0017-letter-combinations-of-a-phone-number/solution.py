class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #We check the edge case
        if len(digits) == 0:
            return []
        #We create a hashmap to keep track pf our numbers and map them to letters
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        res = []
        #We operate the dfs and as the string ar eimmutuable we don't need to pop and we can create new strings on every iteration
        def dfs(i, curr):
            if i >= len(digits):
                res.append(curr)
                return

            for c in hashmap[digits[i]]:
                dfs(i+1, curr+c)
        temp = ""
        dfs(0, temp)
        return res
