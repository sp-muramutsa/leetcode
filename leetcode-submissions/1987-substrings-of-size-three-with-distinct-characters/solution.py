class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_substrings = []
        character_count = len(s)

        for i in range(character_count - 2):
            substring = s[i:i + 3]
            if substring[0] != substring[1] and substring[0] != substring[2] and substring[1] != substring[2]:
                good_substrings.append(substring)
        
        print(good_substrings)
        return len(good_substrings)
        
