#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
from typing import List
# from pprint import pprint


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 0.哨
        board = [['', *b, ''] for b in board]
        board.insert(0, [''] * len(board[0]))
        board.append([''] * len(board[0]))
        # print(board)
        # 1.先将开头字母的索引记录下来
        start_letter = {}
        for x in words:
            start_letter[x[0]] = []
        # print(start_letter)
        for r in range(len(board)):
            for c in range(len(board[0])):
                char = board[r][c]
                if char in start_letter:
                    start_letter[char].append([r, c])
        # print(start_letter)
        # 2.搜索回溯
        def dfs(word, match):
            # print('word:', word, 'match:', match, 'path:', path)
            # pprint(vis)
            # print('####\n\n')
            i, (r, c) = match

            if i == len(word)-1:
                return True

            stacks = []
            vis[r][c] = True
            direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for x, y in direction:
                if board[r+x][c+y] == word[i+1] and not vis[r+x][c+y]:   # 匹配字符，且未访问
                    stacks.append([i+1, (r+x, c+y)])
            result = []
            for i, (r, c) in stacks:                     # 用for循环代替stack，才能回滚访问记录 到分叉点
                result += [dfs(word, [i, (r, c)])]
                vis[r][c] = False
            return any(result)
        
        def exist_letter(board_set, word):          # 判断字母集合是否匹配
            word_set = set(list(word))
            return word_set & board_set == word_set

        board_set = []
        [board_set.extend(x) for x in board]
        board_set = set(board_set)
        ans = []
        for word in words:
            if not exist_letter(board_set, word):                # 如果字母集合不能匹配哪么，直接跳过
                continue
            if start_letter[word[0]] == []:
                continue
            if len(word) == 1:
                ans.append(word)
                continue
            for start_pos in start_letter[word[0]]:
                match = (0, start_pos)  # board的起始坐标，word的匹配字符索引
                vis = [[False] * len(board[0]) for _ in range(len(board))]
                if dfs(word, match):
                    ans.append(word)
                    break           # 如果在一个地方匹配成功，就不再继续
            # print('----')
        return ans
# @lc code=end

