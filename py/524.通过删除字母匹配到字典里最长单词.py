#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # dictionary = [x for x in dictionary if len(x) <= len(s)]    # 仅保留长度小于字符串的字典条目
        pos = [0 for _ in dictionary] # 对应每个dictionary的词的位置

        for ss in s:
            for i, dic in enumerate(dictionary):
                cur_pos = pos[i]
                if cur_pos < len(dic) and dic[cur_pos] == ss:
                    pos[i] += 1
        # print(pos)

        for i, p, d in zip(range(len(pos)), pos, dictionary):   # 只保留完整匹配的
            if p != len(d):
                pos[i] = 0
        # print(pos)

        if max(pos) == 0:               # 边界：都不匹配
            return ''

        if pos.count(max(pos)) == 1:    # 只有一个最长，直接返回
            return dictionary[pos.index(max(pos))]
        else:                           # 多个最长，选出字典序最小的（为了方便，直接排序，但排序会打乱，先挑出最长的）
            dictionary = [dictionary[i] for i, x in enumerate(pos) if x == max(pos)]
            dictionary.sort()
            return dictionary[0]
# @lc code=end

