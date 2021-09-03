class Solution:
    def intToRoman(self, num: int) -> str:
        table = {
            1   :   'I',
            5   :   'V',
            10  :   'X',
            50  :   'L',
            100 :   'C',
            500 :   'D',
            1000:   'M'
        }
        num_t = [1, 5, 10, 50, 100, 500, 1000]
        special_t = {
            4   :   'IV',
            9   :   'IX',
            40  :   'XL',
            90  :   'XC',
            400 :   'CD',
            900 :   'CM'
        }

        result = ''

        for x in num_t[::-1]:
            # 特殊规则
            special_val = self.get_highest_number(num)
            if special_val in special_t:
                result += special_t[special_val]
                num -= special_val
                continue
            # 常规
            n = num // x
            if n != 0:
                num %= x
            result += table[x] * n

            # 提前结束
            if num == 0:
                break
        
        return result
    
    # 获取最高位的值
    def get_highest_number(self, num):
        result = 1
        pre = 0
        while num != 0:
            result *= 10
            pre = num % 10
            num //= 10
        return result * pre // 10

if __name__ == "__main__":
    num_list = [3, 4, 9, 58, 1994]
    for num in num_list:
        print(Solution().intToRoman(num))

# 执行用时 :80 ms, 在所有 Python3 提交中击败了55.78%的用户
# 内存消耗 :14 MB, 在所有 Python3 提交中击败了5.26%的用户


# 题解
# 基于点钱的思路,将4,9的特殊情况都一起对应
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
#         # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
#         nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

#         index = 0
#         res = ''
#         while index < 13:
#             # 注意：这里是等于号，表示尽量使用大的"面值"
#             while num >= nums[index]:
#                 res += romans[index]
#                 num -= nums[index]
#             index += 1
#         return res
