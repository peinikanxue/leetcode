class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0

        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right >= left:
                left = right = 0

        left = right = 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left >= right:
                left = right = 0
        
        return max_len


if __name__ == "__main__":
    s_list = [")()())", "()(()(((", '))))())()()(()', '(()', ')()())', '', '))()', '))(', '()(()', '(()()', '(()))())(', '((()()(()((()', ')(((((()())()()))()(()))(']

    for s in s_list:
        print(Solution().longestValidParentheses(s))
