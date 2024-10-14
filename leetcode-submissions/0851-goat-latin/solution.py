class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        n = len(sentence)
        if n == 0:
            return False
        vowels = ("a", "e", "i", "o", "u")

        hashmap = {}
        words = sentence.split(" ")

        for index, word in enumerate(words):
            hashmap[index] = word
        
        m = len(words)  
        result = ""
        for i in range(m):
            start = hashmap[i][0]
            if start.lower() in vowels:
                result += hashmap[i] + "ma" + "a" * (i + 1) + " "
            else:
                result += hashmap[i][1:] + start + "ma" + "a" * (i + 1) + " "

        
        return result.rstrip()



        
