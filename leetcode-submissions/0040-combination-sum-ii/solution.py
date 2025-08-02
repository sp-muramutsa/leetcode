class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sort the candidates list
        # Edge case if the index exceeds or reaches the end of the list return 
        # Identify the result list 
        # If the sum of the current has been reached add to the result
        # Create a prev number to skip any repeating values and prevent identical siblings
        # Create a for loop to create our tree Staring from current position
        # If the the current value equals previous continue
        # Recursively call the function
        # After backtracking pop from curr
        # Store the prev as current value

        candidates.sort()
        result = []
        def backtrack(i, curr, total):
            if total == target:
                result.append(curr[:])
                return 

            if total > target or i >= len(candidates):
                return

            prev = -1
            for i in range(i, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                backtrack(i+1, curr, total + candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return result
