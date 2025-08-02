class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Edge case is when the sum of the numbers in current list is greater than target, if the index is past length of the list
        # If the sum of the current is equal to the target add it to the result and return
        # Add the current index
        # Recursively call the function with same index
        # After backtracking remove from  the current list and recursively call the next index
        # After defining the above function and running it return the result list
        result = []
        def backtrack(i, curr, total):
            if total == target:
                result.append(curr[:])
                return 

            if i == len(candidates) or total > target:
                return 

            curr.append(candidates[i])
            backtrack(i, curr, total+candidates[i])
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)
        return result
