from typing import List

# 自己做

    # 规律
    # n是在n-1的情况下，两边+()，左右各+()。
    # 注意去除重复。最后的()()...()左右相同，可以特殊处理，中间的重复不易处理。 
    #
    # 1           2           3               4
    # ()          (())        ((()))          (((())))
    #                                         ()((()))
    #                                         ((()))()
    #                         ()(())          (()(()))
    #                                         ()()(())
    #                                         ()(())() 重复
    #                         (())()          ((())())
    #                                         ()(())() 重复
    #                                         (())()()
    #             ()()        (()())          ((()()))
    #                                         ()(()())
    #                                         (()())()
    #                         ()()()          (()()())
    #                                         ()()()()
    #                                         (())(()) 缺失

# 题解
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.result = []

        self.generate('', n, 0)

        return self.result
    
    def generate(self, s, n, sign):
        if n > 0:
            self.generate(s + '(', n-1, sign+1)
        if sign > 0:
            self.generate(s + ')', n, sign-1)

        if sign == 0 and n == 0:
            self.result.append(s)



if __name__ == "__main__":
    n_list = [2, 3, 4]

    for n in n_list:
        print(Solution().generateParenthesis(n))