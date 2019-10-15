# 题解
class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.size = len(s)

        if self.size <= 1:
            return s

        self.max_len = 1
        self.s_max = s[0]

        for m in range(self.size):
            self.cur_len = 0
            self.process(s, m, m)
            self.cur_len = 0
            self.process(s, m, m + 1)

        return self.s_max
    
    def process(self, s, l, r):
        for raduis in range(self.size):
            if l >= 0 and r < self.size and s[l] == s[r]:
                self.cur_len = self.cur_len + 1 if l == r else self.cur_len + 2 # l==r时，只有一个字符，长度只+1
                if self.cur_len > self.max_len:
                    self.max_len = self.cur_len
                    self.s_max = s[l: r + 1]
            else:
                break

            l -= 1
            r += 1

s_list = ['babad', 'cbbd', 'babadabcdcbae', 'ccc', 'cbbd', 'abcba']
for s in s_list:
    print(Solution().longestPalindrome(s))