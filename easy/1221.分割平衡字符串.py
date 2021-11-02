#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        ans = 0

        for x in s:
            if stack == [] or x == stack[0]:
                stack.append(x)
                continue
            elif x != stack[0]:
                stack.pop()
            if stack == []:
                ans += 1
        return ans
# @lc code=end

