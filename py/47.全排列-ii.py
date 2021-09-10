#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        for i, x in enumerate(nums):
            if self.ans == []:
                self.ans.append([x])
                continue
            # print(self.ans)
            while len(self.ans[0]) == i:
                clone = self.ans.pop(0)
                # print(clone)
                for j in range(len(clone) + 1):
                    new_clone = clone.copy()
                    new_clone.insert(j, x)
                    self.ans.append(new_clone)
                # print(self.ans)
        self.ans = set([tuple(x) for x in self.ans])
        self.ans = [list(x) for x in self.ans]
        return self.ans
# @lc code=end

