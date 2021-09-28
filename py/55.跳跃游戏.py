#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i, x in enumerate(nums):
            max_pos = max(i+x, max_pos)
            # print(max_pos, end=' ')
            if max_pos >= len(nums)-1:
                return True
            elif max_pos == i and x == 0:
                return False
        return False
# @lc code=end

