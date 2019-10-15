from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs == [] or '' in strs:
            return ''
        
        i = 0
        prefix = ''

        while True:
            c = strs[0][i] if i < len(strs[0]) else ''  # 如果字符长度够，获取当前字符
            for s in strs:
                if i < len(s) and s[i] != c:    # 如果当前字符长度够
                    return prefix
                elif i >= len(s):
                    return prefix
                    
            prefix += c
            i += 1
        


if __name__ == "__main__":
    strs_list = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
    ]
    for strs in strs_list:
        print(Solution().longestCommonPrefix(strs))