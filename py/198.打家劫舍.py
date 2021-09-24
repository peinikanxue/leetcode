#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] * 3 + nums   # 哨，可以干掉下面的注释
        dp = nums   # 可以直接原地处理
        
        # if len(nums) >= 2:
        #     dp[1] = max(dp[0], dp[1])
        # if len(nums) >= 3:
        #     dp[1] = max(dp[0], dp[1])
        #     dp[2] = max(dp[1], dp[0] + dp[2])
        
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
        return max(dp)
# @lc code=end

