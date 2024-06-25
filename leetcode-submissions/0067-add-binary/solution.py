class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        """
        sum from the end and carry over? string to array, pointers i = a.size, j = b.size, add move forward
        """

        i = len(a) - 1
        j = len(b) - 1
        ans = ""
        rem = 0
        while i >= 0 and j >= 0:
            curr = int(a[i]) + int(b[j]) + rem
            if curr == 2:
                ans = "0" + ans
                rem = 1
            elif curr > 2:
                ans = "1" + ans
                rem = 1
            else:
                ans =  str(curr) + ans
                rem = 0
            i -= 1
            j -= 1

        "if we did not finish one part"
        while i >= 0:
            curr = int(a[i]) + rem
            if(curr == 2):
                ans = "0" + ans
                rem = 1
            elif curr > 2:
                ans = "1" + ans
                rem = 1
            else:
                ans = str(curr) + ans
                rem = 0
            i -= 1

        while j >= 0:
            curr = int(b[j]) + rem
            if(curr > 1):
                ans = "0" + ans
                rem = 1
            elif curr > 2:
                ans = "1" + ans
                rem = 1
            else:
                ans = str(curr) + ans
                rem = 0
            j -= 1

        if rem:
            ans = str(rem) + ans

        return ans
