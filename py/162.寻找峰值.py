#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
# 题解
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m+1] > nums[m]: # 右侧是上坡
                l = m + 1
            else:
                r = m
        return r
# @lc code=end

