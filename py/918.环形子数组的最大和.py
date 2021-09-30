#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def max_or_min_subarray(nums, func=max):
            ans = nums[0]
            tmp = ans
            for i in range(1, len(nums)):
                tmp = func(tmp, 0)
                tmp += nums[i]
                ans = func(tmp, ans)
            return ans
        
        ans = max_or_min_subarray(nums)
        if ans < 0:
            return ans
        ans_min = max_or_min_subarray(nums, func=min)
        ans = max(ans, sum(nums)-ans_min)
        # print(ans, ans_min)
        return ans
# @lc code=end

