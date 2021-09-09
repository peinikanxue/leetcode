#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        nums = [1] + nums
        dp = [float('inf') for _ in range(len(nums))]
        dp[1] = 0

        for i in range(1, len(nums)):
            for k in range(i + 1, min(i + 1 + nums[i], len(nums))):    # 从i开始到i+nums[k]（闭区间，所以再+1），注意避免越界
                dp[k] = min(dp[i] + 1, dp[k])
        # print(dp)
        return dp[-1]
# @lc code=end

