from utils import *

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.boardx = self.init_board(board)
        self.num_dict_origin = {'1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1}
        
        row, col = -1, -1
        while row < 9-1:
            row += 1
            col = -1
            while col < 9-1:
                col += 1
                if self.boardx[row][col][-1] == False:  # 跳过给定值的位置
                    continue
                if self.add_tree(row, col):  # 如果可以继续分支，则继续
                    continue
                else:   # 否则，返回分叉点，剪枝
                    result = self.back_fork(row, col)
                    if result is None:  # 无解情况
                        print('无解')
                        return
                    else:   # 返回分叉点
                        row, col = result
                    self.boardx[row][col].pop(0)
        
        self.fill_board()   # 填充棋盘

    
    def init_board(self, board):
        '''
            记录棋盘，设置标志判别哪些值是固定的
        '''
        board_new = [[[] for _ in range(9)] for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val != '.':
                    board_new[r][c].extend([val, False])
                else:
                    board_new[r][c].extend([True])
        return board_new

    def add_tree(self, row, col):
        '''
            记录判断该位置可以使用的数
        '''
        num_use = self.num_dict_origin.copy()
        # 行
        num_dict = self.num_dict_origin.copy()
        for c in range(9):
            val = self.boardx[row][c][0]
            if val == True:
                continue
            if num_dict[val] > 0:
                num_dict[val] -= 1
                if val in num_use:
                    num_use.pop(val)
            else:
                return False
        # 列
        num_dict = self.num_dict_origin.copy()
        for r in range(9):
            val = self.boardx[r][col][0]
            if val == True:
                continue
            if num_dict[val] > 0:
                num_dict[val] -= 1
                if val in num_use:
                    num_use.pop(val)
            else:
                return False
        # 3x3
        num_dict = self.num_dict_origin.copy()
        R = row // 3
        C = col // 3
        for r in range(3):
            for c in range(3):
                val = self.boardx[R*3+r][C*3+c][0]
                if val == True:
                    continue
                if num_dict[val] > 0:
                    num_dict[val] -= 1
                    if val in num_use:
                        num_use.pop(val)
                else:
                    return False
        # 没有可用的数，加枝失败
        if len(num_use) == 0:
            return False
        # 先清空，再将未使用的数添加到对应位置的列表
        self.boardx[row][col] = []
        for k in num_use.keys():
            self.boardx[row][col].append(k)
        self.boardx[row][col].append(True)
        # print('----------------')     # debug
        # print(f'坐标：({row},{col})')  # debug
        # print(self.boardx[row][col])  # debug
        return True

    def back_fork(self, row, col):
        '''
            返回分叉点位置
            如果循环完都不能确定分叉点，则无解
        '''
        while row >= 0:
            while col >= 0:
                col -= 1
                if self.boardx[row][col][-1]:
                    if len(self.boardx[row][col]) <= 2:  # 只剩一个数和标志，没有数可选时，再往前返回
                        if len(self.boardx[row][col]) > 1:
                            self.boardx[row][col].pop(0)    # 返回的同时清除无效分支
                        continue
                    else:
                        # print(f'<-返回到({row},{col})') # debug
                        return row, col
            row -= 1
            col = 9
        return None
    
    def fill_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.boardx[row][col][0]


if __name__ == "__main__":
    board_list = [
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        [
            [".",".",".",".","5",".",".","1","."],
            [".","4",".","3",".",".",".",".","."],
            [".",".",".",".",".","3",".",".","1"],
            ["8",".",".",".",".",".",".","2","."],
            [".",".","2",".","7",".",".",".","."],
            [".","1","5",".",".",".",".",".","."],
            [".",".",".",".",".","2",".",".","."],
            [".","2",".","9",".",".",".",".","."],
            [".",".","4",".",".",".",".",".","."]
        ],
    ]

    for board in board_list:
        s = Solution()
        s.solveSudoku(board)
        for line in s.board:
            print(line)
