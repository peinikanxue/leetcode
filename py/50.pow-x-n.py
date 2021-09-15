#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1
        elif n == -1:
            return 1 / x
        return self.myPow(x, n // 2) ** 2 * self.myPow(x, n % 2)
# @lc code=end

