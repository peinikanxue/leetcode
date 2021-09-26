#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp, idx = self.head, 0
        while idx < len(word) and word[idx] in tmp: # 找到插入的节点
            if idx == len(word)-1:          # 单词的最后一个字母
                tmp[word[idx]][0] = True
            tmp = tmp[word[idx]][1]
            idx += 1
        for i, x in enumerate(word[idx:]):  # 插入单词
            tmp[x] = [False, {}]
            if i == len(word[idx:])-1:      # 单词的最后一个字母
                tmp[x][0] = True
            tmp = tmp[x][1]


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp, idx, pre_status = self.head, 0, False
        while idx < len(word) and word[idx] in tmp: # 找到插入的节点
            pre_status = tmp[word[idx]][0]
            tmp = tmp[word[idx]][1]
            idx += 1
        return pre_status and idx == len(word)


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp, idx = self.head, 0
        while idx < len(prefix) and prefix[idx] in tmp: # 找到插入的节点
            tmp = tmp[prefix[idx]][1]
            idx += 1
        return idx == len(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

