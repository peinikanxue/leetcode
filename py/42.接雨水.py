#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, H: List[int]) -> int:
        max_h = 0
        record = []
        tmp = []

        # 1.找到闸门
        for i in range(len(H)):
            if H[i] > 0:
                max_h = H[i]
                break

        for i in range(len(H)):
            for j in tmp:       # 清除前面小于最高点的索引
                if H[j] <= H[i]:
                    record[j] = 0

            tmp.append(i)
            record.append(H[i])

            if H[i] >= max_h:
                max_h = H[i]
                tmp.clear()     # 遇到更高的点，清除记录
        # print(record)

        # 2.将闸门两端记录下来
        interval = []
        i = 0
        while i < len(record) and record[i] == 0:
            i += 1
        r = i
        while i < len(record):
            l = r
            while i < len(record) and record[i] == 0:
                i += 1
            if i >= len(record):
                break
            r = i
            interval.append([l, r])
            i += 1
        # print(interval)

        # 3.计算面积
        ans = 0
        for l, r in interval:
            if l == r or r-l == 1:  # 去除两端，以及紧贴在一起的
                continue
            area = (r - l - 1) * min(H[l], H[r])  # w * h
            for i in range(l+1, r):
                h = H[i] if H[i] <= min(H[l], H[r]) else min(H[l], H[r])  # 只减l, r最小的高度
                area -= h
            ans += area
        # print(ans)
        return ans
# @lc code=end

