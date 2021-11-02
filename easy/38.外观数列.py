class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        if n <= 1:  # 边界
            return s

        for _ in range(1, n):
            pre = s[0]
            count = 0
            s2 = ''
            for i, ss in enumerate(s):
                if pre != ss:
                    s2 += str(count) + pre
                    pre = ss
                    count = 0
                count += 1

                if i == len(s) - 1: # 最后一个
                    s2 += str(count) + ss
            s = s2
        return s
        