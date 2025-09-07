class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0

        n = len(s)
        one_digit = 1
        two_digits = 1

        # string ending at i
        for i in range(1, n):

            temp = 0
            # Single character
            if s[i] != "0":
                temp = one_digit

            # Check if we can decode using a double-digit
            if 0 < int(s[i-1]) <= 2 and 0 < int(s[i - 1: i + 1]) <= 26:
                temp += two_digits

            two_digits = one_digit
            one_digit = temp

        return one_digit
