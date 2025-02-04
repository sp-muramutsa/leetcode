class Codec:
    key = 1
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for word in strs:
            length = len(word)
            for i in range(length):
               encoded_string += word[i]
               encoded_string += word[i]
            encoded_string += "01"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        decoded = []
        n = len(s)
        i = 0
        j = 0

        while i < n - 1:
            if s[i] != s[i+1]:
                decoded.append(s[j:i])
                j = i + 2
            i += 2
        
        result = []
        for word in decoded:
            decoded_word = ""
            length = len(word)
            j = 0
            while j < length:
                decoded_word += word[j]
                j += 2
            result.append(decoded_word)

        return result 

                
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
