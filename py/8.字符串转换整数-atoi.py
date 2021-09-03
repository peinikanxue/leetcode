class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0

        is_start = False
        symbol = 1

        for i in range(len(s)):
            c = s[i]

            # 还没开始数字处理
            if not is_start:
                # 跳过前面的空格
                if c == ' ':
                    continue

                # 不为'+','-',数字时
                if c != '+' and c != '-' and (ord(c) < ord('0') or ord(c) > ord('9')):
                    return 0

                # 如果为'+'或'-'，并且还有下一个字符，下一个字符应为数字
                if (c == '+' or c == '-') and i+1 < len(s) and (ord(s[i+1]) < ord('0') or ord(s[i+1]) > ord('9')):
                    return 0

                # 开启数字处理
                if ord('0') <= ord(c) <= ord('9'):
                    is_start = True
                    if i-1 >= 0 and s[i-1] == '-':
                        symbol = -1

            # 数字处理
            if is_start:
                if ord('0') <= ord(c) <= ord('9'):
                    result = result * 10 + int(c)
                else:
                    break
                
        # 加上符号
        result *= symbol

        # 32位取值范围处理
        result = max(min(result, 2**31-1), -2**31)
            
        return result

if __name__ == "__main__":
    s_list = ["42", "   -42", "4193 with words", "words and 987", "-91283472332", "123-"]
    for s in s_list:
        print(Solution().myAtoi(s))
