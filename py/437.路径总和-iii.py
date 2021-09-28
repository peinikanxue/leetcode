#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.ans = 0
        def dfs(node, target_sum, record):
            record.append(0)
            record = list(map(lambda x: x+node.val, record))
            self.ans += record.count(target_sum)
            if node.left:
                dfs(node.left, target_sum, record.copy())
            if node.right:
                dfs(node.right, target_sum, record.copy())
        if root:
            dfs(root, targetSum, [])
        return self.ans
# @lc code=end

