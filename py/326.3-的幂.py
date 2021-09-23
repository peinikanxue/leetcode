#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # dic = {3**i for i in range(0, 20)}
        # return n in dic
        if n == 1:
            return True
        elif n < 1:
            return False
        return n % 3 == 0 and self.isPowerOfThree(n // 3)
# @lc code=end

