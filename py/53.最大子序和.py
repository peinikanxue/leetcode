#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        tmp = ans
        for x in nums[1:]:
            tmp = max(tmp, 0)
            tmp += x
            ans = max(tmp, ans)
        return ans
# @lc code=end

