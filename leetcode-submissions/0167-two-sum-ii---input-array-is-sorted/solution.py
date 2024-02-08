class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)

        i = 0
        j = length - 1


        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            
            elif numbers[i] + numbers[j] < target: # if sum is less than target, move left pointer to the right
                i += 1
                
            else: # if sum is larger than target, move right pointer to the left
                j -= 1
        
        return []
        
        
