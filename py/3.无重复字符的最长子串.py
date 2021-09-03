class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ''
        ss_max = ''
        ss_pos = {}    # 记录每个字母最后的位置
        i = 0
        pre_i = -1      # 记录上次切片的位置

        for x in s:
            if x not in ss_pos:
                ss += x
            else:
                if ss_pos[x] > pre_i:
                    ss = s[ss_pos[x]+1: i+1]
                    pre_i = ss_pos[x]
                else:
                    ss += x
            # 记录字母最后的位置
            ss_pos[x] = i
            # 记录最长子串
            if len(ss) >= len(ss_max):
                ss_max = ss
            i += 1
        
        return len(ss_max)

if __name__ == "__main__":
    s = ['abcabcbb', 'pwwkew', ' ', 'dvdf', 'abba']
    for ss in s:
        print(Solution().lengthOfLongestSubstring(ss))