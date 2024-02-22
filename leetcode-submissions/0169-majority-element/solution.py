class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """"
        Time O(n)
        Space O(n)
        """
        length = len(nums)
        majority_length = length // 2

        hashmap = {}

        for number in nums:
            if number not in hashmap:
                hashmap[number] = 1
            else:
                hashmap[number] += 1
        
        for number, frequency in hashmap.items():
            if frequency > majority_length:
                return number


        
