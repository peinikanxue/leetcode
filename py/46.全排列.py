#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        for i, x in enumerate(nums):    # nums循环
            if self.ans == []:          # 如果空,插入第1个元素
                self.ans.append([x])
                continue
            # print(self.ans)
            while len(self.ans[0]) == i:    # self.ans循环
                clone = self.ans.pop(0)
                # print(clone)
                for j in range(len(clone) + 1): # self.ans中的列表循环,每个空隙都插入当前元素(一共len(clone)+1次)
                    new_clone = clone.copy()
                    new_clone.insert(j, x)
                    self.ans.append(new_clone)
                # print(self.ans)
        return self.ans
# @lc code=end

