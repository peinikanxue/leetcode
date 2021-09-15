#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = a + b
            a, b = b, c
        return c
# @lc code=end

