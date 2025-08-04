class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Create a hashmap that stores list of all possible letters
        # Create the result variable
        # Identify the dfs function 
        # If the Starting_index has reached the end add the path to the result
        # Create a for loop for all possible paths at current index
        # Add them to the path and recursively call the function
        # After backtracking pop from the list
        if len(digits) == 0:
            return []
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
        result = []
        n = len(digits)
        def dfs(starting_index, path):
            if starting_index == n:
                result.append("".join(path.copy()))
                return

            for i in hashmap[digits[starting_index]]:
                path.append(i)
                dfs(starting_index+1, path)
                path.pop()
        
        dfs(0, [])
        return result
