class Solution:
    def maximum69Number (self, num: int) -> int:
        numm = str(num)

        for i in range(len(numm)):
            if numm[i] == '6':
                curr = numm[0:i] + '9' + numm[i+1:len(numm)]                
                return int(curr)
        return num
