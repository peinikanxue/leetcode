#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
# 题解
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exist_1 = False
        for i in range(len(nums)):  # 第一次遍历，将负数处理为1，并先找是否有1
            if nums[i] == 1:
                exist_1 = True
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        if not exist_1:             # 不存在1，直接返回就行
            return 1
        
        for i in range(len(nums)):  # 第二次遍历
            index = abs(nums[i])-1    # 将特殊标记去掉（去掉负号），并且索引从1开始（-1）
            nums[index] = - abs(nums[index])   # 将索引位置的值特殊标记上（添加负号）

        for i in range(len(nums)):  # 第三次遍历，找出前面正数的索引
            if nums[i] > 0:
                return i + 1        # 索引从1开始
        
        return len(nums) + 1


# @lc code=end

