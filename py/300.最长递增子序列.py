#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start\
# 题解
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                dp[i] = max(dp[j]+1, dp[i]) if nums[i] > nums[j] else dp[i]
        return max(dp)
# @lc code=end

