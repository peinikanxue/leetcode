class Solution:
    def isValid(self, s: str) -> bool:

        s_dict = {'(':')', '[':']', '{':'}'}
        
        stack = []

        for ss in s:
            if ss in s_dict:
                stack.append(ss)
            else:
                if not stack:   # 空栈
                    return False
                tmp_char = stack.pop()
                if ss != s_dict[tmp_char]:
                    return False
        if stack:   # 还剩有括号
            return False
        else:
            return True


if __name__ == "__main__":
    s_list = ["()", "()[]{}", "(]", '[', '{[()]}', '{[()()]}']

    for s in s_list:
        print(Solution().isValid(s))