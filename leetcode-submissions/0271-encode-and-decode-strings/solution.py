class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = []

        for word in strs:
            for char in word:
                encoded_string.append(char)
                encoded_string.append(char)
            encoded_string.append("01")

        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""

        n = len(s)
        decoded_strings = []
        string = []

        i = 0
        while i < n - 1:
            while s[i] == s[i + 1]:
                string.append(s[i])
                i += 2

            decoded_strings.append("".join(string))
            string = []
            i += 2

        return decoded_strings


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

