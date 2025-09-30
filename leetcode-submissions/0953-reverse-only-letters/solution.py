class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        word_list = list(s)

        right = len(word_list) - 1
        left = 0

        while left < right:

            if ((ord(word_list[left]) not in range(65,91)) and (ord(word_list[left]) not in range(97,123))):
                left += 1
            elif ((ord(word_list[right]) not in range(65,91)) and (ord(word_list[right]) not in range(97,123))):
                right -= 1

            else:
                helper = word_list[left]
                word_list[left] = word_list[right]
                word_list[right] = helper

                left += 1
                right -= 1

        return "".join(word_list)
        
