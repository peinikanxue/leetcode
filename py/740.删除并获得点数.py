#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 1.将原问题转为打家劫舍
        def convert(nums):
            nums.sort()
            # 空缺补0
            tmp = nums[0]
            idx = 1
            while idx < len(nums):
                if nums[idx] > tmp + 1:
                    # nums.insert(idx, 0)
                    nums.insert(idx, -idx)  # 为了区分，补负值方便处理
                    idx += 1
                tmp = nums[idx]
                idx += 1
            # print(nums)
            nums = [k*v for k,v in Counter(nums).items()]
            nums = list(map(lambda x: x if x > 0 else 0, nums)) # 将负数改为0
            # print(nums)
            return nums

        # 2.打劫
        def rob(nums):
            nums = [0] * 3 + nums   # 哨，可以干掉下面的注释
            dp = nums   # 可以直接原地处理
            
            for i in range(3, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
            return max(dp)

        nums = convert(nums)
        return rob(nums)
# @lc code=end

