#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        
        cost.append(0)  # 哨
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return cost[-1]
# @lc code=end

