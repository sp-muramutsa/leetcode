class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(w):
            return w[::-1]

        words = s.split(" ")
        result = []

        for word in words:
            result.append(reverse(word))

        return " ".join(word for word in result)

