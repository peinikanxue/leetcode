#
# @lc app=leetcode.cn id=41 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
# 题解
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()     # 排序
        self.ans = []
        self.dfs(candidates, target, 0, [])
        return self.ans

    def dfs(self, candidates, target, idx, record):
        # if idx == len(candidates):                                    # 不再需要：只有一个元素时，影响了下面target==0的分支执行
        #     return
        # if sum(candidates[idx:]) < target:                            # 不再需要：有candiates[i] > target做剪枝就够了
        #     return
        if target == 0:
            self.ans.append(record[:])                                  # deep copy
            return
        
        for i in range(idx, len(candidates)):
            if candidates[i] > target:                                  # 剪枝
                break

            if i > idx and candidates[i - 1] == candidates[i]:          # *核心剪枝：将同一层数值相同的结点，第2、3、...个结点都跳过
                continue

            record.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i + 1, record)   # 使用当前元素
            record.pop()


# @lc code=end

