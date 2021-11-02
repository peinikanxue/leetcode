class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s

        out = ''
        length = len(s)
        col1 = 2 * numRows - 2
        col2 = 0

        for r in range(numRows):
            i = r
            
            if i >= len(s): # 边界处理
                break

            while True:
                if col1 != 0:
                    out += s[i]
                    i += col1
                    if i >= length:
                        break

                if col2 != 0:    
                    out += s[i]
                    i += col2
                    if i >= length:
                        break
            col1 -= 2
            col2 += 2
        
        return out
        
if __name__ == "__main__":
    s_list = ['LEETCODEISHIRING', 'LEETCODEISHIRING', 'AB', 'A', 'AB']
    numRows_list = [3, 4, 1, 2, 3]

    for i in range(len(s_list)):
        print(Solution().convert(s_list[i], numRows_list[i]))