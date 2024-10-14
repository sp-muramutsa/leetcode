class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        result = ""
        carry = 0
        m, n = len(num1) - 1, len(num2) - 1
        i = j = 0

        while  m >= 0 or n >= 0:
            # convert to int
            x1 =  ord(num1[m]) - ord("0") if m >= 0 else 0
            x2 = ord(num2[n]) - ord("0") if n >= 0 else 0

            # calculate the summation, carry, and the result
            value = (x1 + x2 + carry ) % 10
            carry = (x1 + x2 + carry ) // 10
            result += str(value)
            m -= 1
            n -= 1
        
        if carry:
            result += str(carry)
        
        return result[::-1]

        

        
