class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        list_s = []
        for i in s:
            if i.isalnum():
                list_s.append(i)
        l,r = 0, len(list_s)-1
        while l <= r:
            if list_s[r].lower() != list_s[l].lower():
                return False
            l += 1
            r -= 1
        return True
