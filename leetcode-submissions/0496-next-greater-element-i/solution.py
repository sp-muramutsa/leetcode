class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a result list 
        # Create hashmap key will be number and value will be index
        # Iterate through the nums1
        # Get the index in nums2 using hashmap and if there exists right index and it is greater than current number add it to the reuslt, else add -1
        
        hashmap = {}
        result = []
        for i, n in enumerate(nums2):
            hashmap[n] = i
            
        for num in nums1:
            idx = hashmap[num]
            p1 = idx
            if idx == len(nums2) - 1:
                result.append(-1)
                continue

            while True:
                if p1 == len(nums2) - 1:
                    result.append(-1)
                    break
                if nums2[p1+1] > nums2[idx]:
                    result.append(nums2[p1+1])
                    break
                p1 += 1

            
        return result
