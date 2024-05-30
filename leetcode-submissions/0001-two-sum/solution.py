class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(logn)
        """

        hashmap = {}

        for index, number in enumerate(nums):
            hashmap[index] = number

        hashmap = dict(sorted(hashmap.items(), key=lambda x:x[1]))  
        hashmap_values = list(hashmap.values())
        hashmap_keys = list(hashmap.keys())
        print(hashmap)

        l, r = 0, len(nums) - 1

        while l < r:
            print(l, r)
            if hashmap_values[l] + hashmap_values[r] < target: 
                l += 1

            elif hashmap_values[l] + hashmap_values[r] > target:
                r -= 1
            
            else:
                return [hashmap_keys[l], hashmap_keys[r]]



        
