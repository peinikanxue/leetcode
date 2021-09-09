#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
# 题解
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' ' + s, ' ' + p # 哨
        m, n = len(s), len(p)
        dp = [[False for _ in range(m)] for _ in range(n)]

        dp[0][0] = True

        for i in range(1, n):   # 题解抄来，单独处理*开头的情况（后面就不再管了）
            if p[i] == '*':
                dp[i][0] = True
            else:
                break

        for i in range(1, n):
            for j in range(1, m):
                # dp[i][j] = (
                #     (p[i] in (s[j], '?') and (dp[i-1][j-1] or (p[i-1] == '*' and dp[i-1][j])))
                #     or (p[i] == '*' and (dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]))
                # )
                dp[i][j] = (
                    (p[i] in (s[j], '?') and (dp[i-1][j-1]))
                    or (p[i] == '*' and (dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]))
                )
        
        # print('\t'.join(list(s)))
        # for i in range(n):
        #     print(p[i], end=' ')
        #     for j in range(m):
        #         print(f'{"T" if dp[i][j] else " "}', end='\t')
        #     print()
        return dp[-1][-1]
# @lc code=end

