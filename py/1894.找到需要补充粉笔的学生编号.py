#
# @lc app=leetcode.cn id=1894 lang=python3
#
# [1894] 找到需要补充粉笔的学生编号
#

# @lc code=start
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)

        for i, x in enumerate(chalk):
            if k == 0:      # 上一个同学用完了,当前同学一支没有
                return i
            k -= x
            if k < 0:       # 当前同学不够用
                return i
# @lc code=end

