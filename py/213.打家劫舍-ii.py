#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:                  # 只有一个元素
            return nums[0]
        origin_nums = nums

        # 第一遍
        nums = [0] * 3 + origin_nums[:-1]   # 哨，可以干掉下面的注释
        dp = nums               # 可以直接原地处理
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])

        max_val = max(dp)

        # 第二遍
        nums = [0] * 3 + origin_nums[1:]
        dp = nums
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])

        max_val = max(max_val, max(dp))

        return max_val
# @lc code=end

