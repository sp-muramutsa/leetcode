class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Get the smallest length of the string
        # Create a variable for prefix string
        # For loop for the range of the minimum number
        # If the string is present in all strings ass it to the res else break
        # Return the string
        length = float("inf")
        for i, n in enumerate(strs):
            length = min(length, len(n))

        print(length)
        
        if length < 1:
            return ""

        res = ""

        for i in range(length):
            char = strs[0][i]
            end = False
            for j in range(len(strs)):
                if strs[j][i] != char:
                    end = True
                    break

            if not end:
                res += strs[0][i]
            if end:
                break

        return res
