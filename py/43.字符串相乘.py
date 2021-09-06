#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = []
        ACC = []
        CF = []

        if num1 == '0' or num2 == '0':      # 边界：乘0
            return '0'

        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]         # 逆序，方便从右往左开始

        for c in range(1, len(num1) + len(num2)):   # c从1开始，行才能从0开始，位数不超过两个数位的总和
            ACC.extend(CF)  # 进位加入累加器
            CF.clear()      # 清空上一次的进位
            for r in range(min(c, len(num2))):  # r-c中r不超过len(num2)
                if c-r-1 < len(num1):           # r-c中c不超过len(num1)
            #         print(f'{r+1}-{c-r-1+1}') # debug 索引从1开始，便于查看
                    multi = int(num2[r]) * int(num1[c-r-1])
                    cur = multi % 10    # 取个位
                    cf = multi // 10    # 取十位
                    ACC.append(cur)
                    if cf != 0:
                        CF.append(cf)
                    # print(f'{r}-{c-r-1} v:{num2[r]}*{num1[c-r-1]} m:{multi}')           # debug 索引从0开始
            # print('---')                      # debug
            add = sum(ACC)
            cur = add % 10
            cf = add // 10
            # print(f'ACC:{ACC}, CF:{CF}, cur:{cur}, ans:{ans}\n========')      # debug
            ACC.clear()
            ans.insert(0, str(cur))
            if cf != 0:
                CF.append(cf)   # 进位
        if CF != []:            # 如果进位还剩
            # print(f'CF:{CF}')
            ans.insert(0, str(sum(CF)))
        return ''.join(ans)
# @lc code=end

