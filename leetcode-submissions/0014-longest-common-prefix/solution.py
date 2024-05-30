class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def prefix(word1 : str, word2: str):
            length = min(len(word1), len(word2))
            common_prefix = ""

            for i in range(length):
                if word1[i] == word2[i]:
                    print("Yes")
                    common_prefix = common_prefix + word1[i]
                else:
                    break
                    
            return common_prefix
            

        length = len(strs)
        common_prefix = strs[0]
        for i in range(1, length):
            common_prefix = prefix(common_prefix, strs[i])
        
        return common_prefix


        
    
