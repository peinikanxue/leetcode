class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not haystack and not needle or not needle: # 边界：都为空字符串，或模式串为空
            return 0
        
        next_list = self.get_next(needle)
        pos = -1

        i = j = 0
        while j < len(needle) and len(haystack) >= len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    pos = i - j
                    break
            else:
                j = next_list[j]
                if j == -1:
                    i += 1
                    j = 0
                if len(haystack) - i < len(needle) - j: # 剩余子串不够匹配
                    break
        return pos


    def get_next(self, s):
        i = 0
        j = -1
        next_list = [-1]

        while i < len(s) - 1:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                next_list.append(j)
            else:
                j = next_list[j]
        return next_list


if __name__ == "__main__":
    haystack_list = ['hello', '', '', 'a', 'aaa', 'aaaaa', 'aabaaabaaac']
    needle_list = ['ll','', 'a', '', 'aaa', 'bba', 'aabaaac']

    for haystack, needle in zip(haystack_list, needle_list):
        print(Solution().strStr(haystack, needle))
