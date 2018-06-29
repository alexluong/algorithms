class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        costArr = [None] * length
        
        costArr[0] = cost[0]
        costArr[1] = cost[1]

        for i in range(2, length):
            costArr[i] = min(costArr[i - 1], costArr[i - 2]) + cost[i]

        return min(costArr[length - 2], costArr[length - 1])


print(Solution().minCostClimbingStairs([10, 15, 20]))