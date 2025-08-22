class Solution:
    def reverseVowels(self, s: str) -> str:
        result = []
        for i in s:
            result.append(i)
        l, r = 0, len(s) - 1
        vowels = set()
        vowels.add("a")
        vowels.add("i")
        vowels.add("u")
        vowels.add("o")
        vowels.add("e")

        while l < r:
            if result[l].lower() in vowels and result[r].lower() in vowels:
                result[l], result[r] = result[r], result[l]
                l += 1
                r -= 1

            elif result[l].lower() in vowels:
                r -= 1

            elif result[r].lower() in vowels:
                l += 1

            else:
                l += 1
                r -= 1

        return "".join(result)
