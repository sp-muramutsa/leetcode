class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        Intuition: put word and abbr on line and iterate while checking. If you meet a numeric value in abbr. Pause and parse it. After parsing it check to see if what's beyond it in abbr is the same as in the original word. If not, return False, else keep iterating.
        """
        length1 = len(word)
        length2 = len(abbr)
        i, j = 0, 0

        while i < length1 and j < length2: 
            
            if word[i] == abbr[j]:
                i += 1
                j += 1
                
            elif abbr[j].isnumeric():
                if abbr[j] == "0":
                    return False
                k = j 
                number_str = ""
                
                while k < length2 and abbr[k].isnumeric():
                    number_str += abbr[k]
                    k += 1
                    
                number = int(number_str)
                i += number            
                j = k

                # if i > length1:
                #     return False
            else:
                return False

        return i == length1 and j == length2



        
