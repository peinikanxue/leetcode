# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if s == p == '':
#             return True
#         if p == '':
#             return False

#         i = 0
#         j = 0
#         is_star = False
#         is_dot = False
#         star_char = ''

#         while i < len(s) and j < len(p):
#             # 如果字符是'.'，则开启通配。
#             if p[j] == '.':
#                 is_dot = True
#             # 如果后一个字符是'*'，则开启匹配前一个字符。
#             if j+1 < len(p) and p[j+1] == '*':
#                 is_star = True
#                 star_char = p[j]

#             # .*
#             if is_dot and is_star:
#                 while i < len(s) and s[i] != p[j]:
#                     i += 1
#                 j += 2  # 跳过*
#             # .
#             elif is_dot:
#                 i += 1
#                 j += 1
#             # *
#             elif is_star:
#                 while i < len(s) and s[i] == p[j]:
#                     i += 1
#                 j += 2  # 跳过*
#                 # 跳过p中*后重复的字符,处理"aaaa","a*aa"的情况.
#                 while j < len(p) and p[j] == star_char:
#                     j += 1
#             # 正常字符串匹配
#             else:
#                 i += 1
#                 j += 1

#             # 清除标志
#             is_star = False
#             is_dot = False
        
#         # 是否匹配完全
#         if i == len(s) and j == len(p):
#             return True
#         else:
#             return False

# 题解
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or  # '*' 0个的情况
                    first_match and                     # '*' 1个的情况
                    self.isMatch(text[1:], pattern))    # ‘*’ 1个以上的情况
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])  # 没有'*'的情况

    
if __name__ == "__main__":
    s_list = ["aa", "aa", "ab", "aab", "mississippi", "aaaa", "aaa"]
    p_list = ["a", "a*", ".*", "c*a*b", "mis*is*p*.", "a*aa", "ab*a*c*a"]

    for i in range(len(s_list)):
        print(Solution().isMatch(s_list[i], p_list[i]))
        