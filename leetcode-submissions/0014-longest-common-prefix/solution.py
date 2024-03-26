class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def compare(word1, word2):
            min_len = min(len(word1), len(word2))
            prefix = ""
            for i in range(min_len):
                if word1[i] == word2[i]:
                    prefix += word1[i]
                else:
                    break
            return prefix

        prefix = strs[0]
        length = len(strs)

        for i in range(length):
            prefix = compare(prefix, strs[i])

        return prefix


        


        

      
            


       
        
        
