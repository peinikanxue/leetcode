class Solution:
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        result = 0

        INT_MIN = -2**31
        INT_MAX = 2**31-1

        # 保留符号
        is_negative = -1 if x < 0 else 1
        x = abs(x)

        while x:
            result = result * 10 + x % 10
            x //= 10

            # 判断是否越界
            if result*is_negative < INT_MIN or result*is_negative > INT_MAX:
                return 0

        # 添加符号
        result *= is_negative

        return result
        

if __name__ == "__main__":
    x_list = [123, -123, 120]
    for x in x_list:
        print(Solution().reverse(x))
