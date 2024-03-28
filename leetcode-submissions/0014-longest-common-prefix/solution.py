class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        """
        Time complexity: O(nm + nlog(n))
        Space complexity: O(m + n)
        """

        def compare_prefixation(word1: str, word2: str) -> bool:
            prefix = ""
            length1, length2 = len(word1), len(word2)
            min_len = min(length1, length2)

            for i in range(min_len):
                if word1[i] == word2[i]:
                    prefix += word[i]
                else:
                    break
            return prefix
            
            
        
        prefix = strs[0]
        for word in strs[1:]:
            prefix = compare_prefixation(word, prefix)
        
        return prefix

        


        

      
            


       
        
        
