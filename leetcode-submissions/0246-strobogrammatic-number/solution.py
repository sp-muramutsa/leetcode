class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        Intuition: We store all strobogrammatic numbers in a hashmap. We use two pointers one from start and another from end to check if the left and right digit are each other's mirror images. If not, then we return False.
        3 conditions for the left and right to be each others mirror images:
        - left is among the digits with images
        - right is among the digits with images
        - left is right's image (or right is left's image)
        """

        hashmap = {"6": "9", "9": "6", "8": "8", "1": "1", "0":"0"}

        l, r = 0, len(num) - 1

        while l <= r:
            if num[l] not in hashmap or num[r] not in hashmap  or num[l] != hashmap[num[r]]: #  can also be num[r] != hashmap[num[l]]
                return False
            l += 1
            r -= 1
        
        return True
