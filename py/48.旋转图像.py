#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(M)
        for l in range(n // 2):         # layer
            for i in range(n - l*2-1):
                tmp = M[l][l+i]
                M[l][l+i] = M[n-1-i-l][l]
                M[n-1-i-l][l] = M[n-1-l][n-1-i-l]
                M[n-1-l][n-1-i-l] = M[l+i][n-1-l]
                M[l+i][n-1-l] = tmp
# @lc code=end

