class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # Solution 4/4: Bottom down DP, Constant space
        n = len(cost)
        one_step_back = 0
        two_steps_back = 0
        res = 0

        for i in range(2, n + 1):
            res = min(one_step_back + cost[i - 1], two_steps_back + cost[i - 2])
            two_steps_back = one_step_back
            one_step_back = res

        return res

