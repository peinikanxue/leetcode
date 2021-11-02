from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], num: int) -> int:
        # digits = list(map(int, digits))
        digits = list(map(int, digits))
        num_list = list(map(int, list(str(num))))
        count = 0
        n1 = len(digits)    # 可选择数字个数
        n2 = len(str(num))    # 目标值的位数

        # 1.处理最高位的情况
        def find_min(digits, target):   # 找到小于等于目标值的位置(digits有序) (替换为字典更舒服)
            l, r = 0, len(digits)-1
            while l < r:
                m = (l + r) // 2
                if digits[m] == target:
                    return m + 1    # 索引值少-1
                elif digits[m] > target:
                    r = m - 1
                elif digits[m] < target:
                    l = m + 1
            l = l if digits[l] > target else l + 1
            return l
        
        # 1.1 判断是否存在位数一样 且小于目标值的数
        is_all_usable = True    # num的每一位都能找到对应的数
        for x in num_list:
            if digits[find_min(digits, x) - 1] != x:
                is_all_usable = False
                break
        is_max_usable = find_min(digits, num_list[0]) # 最高位能找到数

        # 1.2 如果存在，可以计算小于目标值的数量
        if is_all_usable:   # 每一位都可找到
            count += 1
        if is_max_usable:   # 最大的一位能找到
            num_size = len(num_list)
            digits_size = len(digits)
            prob = 0
            for i in range(num_size):    # 不同位的可能性相乘
                x = num_list[i]
                idx = find_min(digits, x)
                idx_copy = idx
                idx = max(0, idx - 1 if digits[idx-1] == x else idx)
                prob += idx * digits_size ** (num_size - 1 - i)
                if digits[idx_copy - 1] != x:   # 当前位不能在digital中找到时，下一位没必要再循环，因为都被统计在内了
                    break
            count += prob

        # 2.n少一位的情况
        for nn2 in range(1, n2):    # 解决高位为'0'的情况
            count += n1 ** (nn2)
        return count



if __name__ == '__main__':
    digits_list = [
        ['1', '7'],
        ["2","3","4","6","8"],
        ["3","4","5","6"],
        ['5', '7', '8'],
        ['7'],
        ["1","3","5","7"],
        ["1","4","9"],
    ]
    n_list = [
        231,
        61,
        64,
        59,
        8,
        100,
        1000000000,
    ]

    for d, l in zip(digits_list, n_list):
        print(Solution().atMostNGivenDigitSet(d, l))