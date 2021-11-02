#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
from typing import List
from collections import defaultdict
from math import factorial

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
        
        ans = 0
        for i, (x1, y1) in enumerate(points):
            dis_dict = defaultdict(list)
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                dis = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
                dis_dict[dis].append([x2, y2])
            for _, v in dis_dict.items():   # 集中计算排列数
                if len(v) > 1:
                    ans += factorial(len(v)) // factorial(len(v) - 2)
            # print(dis_dict)
        return ans
# @lc code=end

