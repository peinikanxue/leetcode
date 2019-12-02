from utils import *

# 超时
# import itertools

# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:

#         if not s:
#             return []
        
#         result = []

#         for w in itertools.permutations(words):
#             result.extend(self.kmp(s, ''.join(w)))

#         return list(set(result))
    
#     def kmp(self, s: str, pattern: str):

#         if not s and not pattern or not pattern: # 边界：都为空字符串，或模式串为空
#             return []
        
#         next_list = self.get_next(pattern)
#         pos = []

#         i = j = 0
#         while j < len(pattern) and len(s) - i >= len(pattern) - j:
#             if s[i] == pattern[j]:
#                 i += 1
#                 j += 1
#                 if j == len(pattern):
#                     pos.append(i - j)
#                     i = i - len(pattern) + 1
#                     j = 0
#             else:
#                 j = next_list[j]
#                 if j == -1:
#                     i += 1
#                     j = 0
#                 if len(s) - i < len(pattern) - j: # 剩余子串不够匹配
#                     break
#         return pos


#     def get_next(self, s):
#         i = 0
#         j = -1
#         next_list = [-1]

#         while i < len(s) - 1:
#             if j == -1 or s[i] == s[j]:
#                 i += 1
#                 j += 1
#                 next_list.append(j)
#             else:
#                 j = next_list[j]
#         return next_list





# from collections import Counter

# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:

#         if not s or not words:   # 边界：s,words无字符
#             return []
        
#         result = []
#         pos_dict = {}
#         words_dict = Counter(words)

#         for word in words:
#             for index in self.kmp(s, word):
#                 pos_dict[index] = word
        
#         for key in sorted(pos_dict):
#             i = key
#             w_dict = words_dict.copy()
#             while i <= len(s):
#                 if i in pos_dict and pos_dict[i] in w_dict:   # 位置在字典中，并且位置对应的字符串存在可用词典中
#                     w_dict[pos_dict[i]] -= 1    # 可用词的词典计数-1
#                     if w_dict[pos_dict[i]] == 0:  # 可用词的词典计数为0，删除
#                         del w_dict[pos_dict[i]]
#                 else:
#                     if not w_dict:      # 满足匹配(后一个子字符串属于字典)
#                         result.append(key)
#                     break
                
#                 i = i + len(pos_dict[i])

#         return result

    
#     def kmp(self, s: str, pattern: str):

#         if not s and not pattern or not pattern: # 边界：都为空字符串，或模式串为空
#             return []
        
#         next_list = self.get_next(pattern)
#         pos = []

#         i = j = 0
#         while j < len(pattern) and len(s) - i >= len(pattern) - j:
#             if s[i] == pattern[j]:
#                 i += 1
#                 j += 1
#                 if j == len(pattern):
#                     pos.append(i - j)
#                     i = i - len(pattern) + 1
#                     j = 0
#             else:
#                 j = next_list[j]
#                 if j == -1:
#                     i += 1
#                     j = 0
#                 if len(s) - i < len(pattern) - j: # 剩余子串不够匹配
#                     break
#         return pos


#     def get_next(self, s):
#         i = 0
#         j = -1
#         next_list = [-1]

#         while i < len(s) - 1:
#             if j == -1 or s[i] == s[j]:
#                 i += 1
#                 j += 1
#                 next_list.append(j)
#             else:
#                 j = next_list[j]
#         return next_list



# 审题后，words长度一样，s由多个word长度的单词组成
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:  # 边界：空s或空words
            return []
        
        result = []
        used_words_dict = Counter(words)

        i = 0                               # 索引
        len_word = len(words[0])            # 一个词的长度
        len_words = len_word * len(words)   # 所有词的总长度
        count = 0                           # 计数已用了几个词
        uwd = used_words_dict.copy()        # 复制的表

        while i < len(s):
            word = s[i:(i+len_word)]
            i += len_word

            if word in uwd:
                uwd[word] -= 1
                count += 1
                if uwd[word] == 0:
                    del uwd[word]
                if not uwd:                 # 表中单词已使用完
                    result.append(i - len_words)
            else:
                uwd = used_words_dict.copy()
                i = i - (count + 1) * len_word + 1
                count = 0
                if i > len(s) - len_words:
                    break
        
        return result


if __name__ == "__main__":
    s_list = [
        'barfoothefoobarfoomanfooabbarfoo',
        "wordgoodgoodgoodbestword",
        "foobarfoobar",
        "",
        "abc",
        "",
        "aaa",
        "a",
        "aaaaaaaa",
        "lingmindraboofooowingdingbarrwingmonkeypoundcake",
    ]

    words_list = [
        ["foo","bar"],
        ["word","good","best","good"],
        ["foo","bar"],
        [],
        [],
        ["a"],
        ['a', 'a'],
        ["a"],
        ['aa', 'aa', 'aa'],
        ["fooo","barr","wing","ding","wing"],
    ]
    
    for s, words in zip(s_list, words_list):
        print(Solution().findSubstring(s, words))
