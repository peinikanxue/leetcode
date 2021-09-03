#
# @lc app=leetcode.cn id=41 lang=python3
#
# [39] 组合总和
#

# @lc code=start
# 题解
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.dfs(candidates, target, 0, [])
        return self.ans

    def dfs(self, candidates, target, idx, record):
        if idx == len(candidates):
            return
        if target == 0:
            self.ans.append(record.copy())                              # 防止record被接下来的操作覆盖
            return
        
        self.dfs(candidates, target, idx + 1, record)                   # 跳过该元素

        if target - candidates[idx] >= 0:
            record.append(candidates[idx])                              # push当前元素
            self.dfs(candidates, target-candidates[idx], idx, record)   # 使用当前元素
            record.pop()                                                # pop"最后"元素（递归的最里层依次返回，pop的最后其实就是当前元素）


# @lc code=end

