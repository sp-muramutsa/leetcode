class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []

        for word in s.split(" "):
            reverse_list = list(word)
            
            left = 0
            right = len(reverse_list) - 1

            while left < right:
                helper = reverse_list[left]
                reverse_list[left] = reverse_list[right]
                reverse_list[right] = helper
                left += 1
                right -= 1

            word_list.append("".join(reverse_list))
            word_list.append(" ")
        
        
        return "".join(word_list[0:-1])
        
