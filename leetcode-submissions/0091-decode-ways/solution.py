class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        two_digits = 1
        one_digit = 1 if s[0] != "0" else 0

        for i in range(1, n):

            # One digit can't be decoded if it is 0
            temp = 0
            if s[i] != "0":
                temp += one_digit

            # 1 <= x <= 26
            if s[i - 1] != "0" and int(s[i - 1 : i + 1]) <= 26:
                temp += two_digits

            two_digits = one_digit
            one_digit = temp

        return one_digit

