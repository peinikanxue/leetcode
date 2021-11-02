#
# @lc app=leetcode.cn id=41 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        if len(v1) > len(v2):
            v2 += [0] * (len(v1) - len(v2))
        else:
            v1 += [0] * (len(v2) - len(v1))
        
        # print(v1)
        # print(v2)

        for x1, x2 in zip(v1, v2):
            if x1 > x2:
                return 1
            elif x1 < x2:
                return -1
            else:
                continue
        return 0


# @lc code=end

