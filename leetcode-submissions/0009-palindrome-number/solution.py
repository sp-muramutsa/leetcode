class Solution:
    def isPalindrome(self, x: int) -> bool:
        #parse or mod stuff
        num = str(x)
        n = len(num)
        front, back = 0, n - 1
        while front < back:
            if num[front] != num[back]:
                return False
            front += 1
            back -= 1
        return True
