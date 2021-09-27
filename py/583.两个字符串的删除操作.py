#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
import bisect
from collections import defaultdict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pos_list = []
        pos2_dict = defaultdict(list)
        for i, x in enumerate(word2):
            pos2_dict[x].append(i)
        for x in word1:
            if x in word2:
                pos_list.extend(pos2_dict[x][::-1])
        # print(pos_list, pos2_dict)
        
        tails = []
        for pos in pos_list:
            idx = bisect.bisect_left(tails, pos)
            if idx == len(tails):   # 大于最后一个值，插入
                tails.append(pos)
            else:                   # 小于其中的值，替换
                if pos < tails[idx]:
                    tails[idx] = pos
        max_subsequence_len = len(tails)
        return len(word1) - max_subsequence_len + len(word2) - max_subsequence_len

# @lc code=end

