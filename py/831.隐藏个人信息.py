#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

# @lc code=start
class Solution:
    def maskPII(self, S: str) -> str:

        if '@' in S:
            return self.mask_email(S)
        else:
            return self.mask_phone(S)


    def mask_email(self, S):
        S = S.lower()
        name, company = S.split('@')
        return name[0] + '*****' + name[-1] + '@' + company



    def mask_phone(self, S):
        filter_list = ['+', '-', '(', ')', ' ']
        for f in filter_list:
            S = S.replace(f, '')
        if len(S) <= 10:
            prefix = '***-***-'
        else:
            prefix = '+' + '*'*(len(S)-10) + '-***-***-'
        return prefix + S[-4:]
        
# @lc code=end

