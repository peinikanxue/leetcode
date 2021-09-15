#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1

        dp = [0, 1, 1]
        ans = 0
        for i in range(3, n+1):
            ans = dp[0] + dp[1] + dp[2]
            dp[0], dp[1], dp[2] = dp[1], dp[2], ans
        return ans
# @lc code=end

