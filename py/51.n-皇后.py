#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List
from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # 根据Q的位置列表，将位置占领
        def update_vis(vis, Q_pos):
            direction = [(+1, +1), (-1, -1), (-1, +1), (+1, -1)]
            rows, cols = [x[0] for x in Q_pos], [x[1] for x in Q_pos]
            vis_pos, n = [], len(vis)
            [[[vis_pos.append((row+x*rate, col+y*rate)) for rate in range(n) if 0<=row+x*rate<n and 0<=col+y*rate<n] for x, y in direction] for row, col in Q_pos]
            vis_pos = set(vis_pos)

            for i in range(n):
                for j in range(n):
                    if i in rows or j in cols or (i, j) in vis_pos:
                        vis[i][j] = True
                    else:
                        vis[i][j] = False
            return vis

        # 搜索回溯
        def dfs(vis, Q_pos, row, ans):
            '''
                棋盘，是否被占据，棋盘边长，已经放置了几个，第几行
            '''
            n = len(vis)
            if len(Q_pos) == n:                 # 满足条件，加入答案
                # print(Q_pos)
                ans.append(deepcopy(Q_pos))
            if row >= n:
                return

            # vis = get_vis(vis, Q_pos)   # 占据位置
            for col in range(n):
                if not vis[row][col]:
                    # print(f'{row},{col}')
                    Q_pos.append((row, col))
                    vis = update_vis(vis, Q_pos)   # 更新占据的位置
                    # print(row, ' append:', Q_pos)
                    dfs(vis, Q_pos, row+1, ans) # 前往下一层
                    Q_pos.pop()                 # 回溯
                    vis = update_vis(vis, Q_pos)   # 更新占据的位置
                    # print(row, ' pop:', Q_pos)

        # 1.搜索
        vis = [[False] * n for _ in range(n)]
        ans = []
        dfs(vis, [], 0, ans)
        # print(ans)

        # 2.转换格式
        ans_format = [['.'*n for _ in range(n)] for _ in range(len(ans))]
        for i, Q_pos in enumerate(ans):
            for row, col in Q_pos:
                ans_format[i][row] = ans_format[i][row][:col] + 'Q' + ans_format[i][row][col+1:]

        return ans_format
# @lc code=end

