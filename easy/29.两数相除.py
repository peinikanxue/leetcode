# 超时
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:

#         count = 0
#         symbol = (dividend < 0) ^ (divisor < 0)

#         dividend = abs(dividend)
#         divisor = abs(divisor)
        
#         while dividend >= divisor:
#             dividend -= divisor
#             count += 1
        
#         if symbol:
#             count = -count
        
#         return count


# 题解
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        symbol = (dividend < 0) ^ (divisor < 0)
        count = 0
        result = 0

        dividend = abs(dividend)
        divisor = abs(divisor)
        
        while dividend >= divisor:
            count += 1
            divisor <<= 1

        while count > 0:
            count -= 1
            divisor >>= 1
            result <<= 1
            if dividend >= divisor:
                result += 1
                dividend -= divisor

        if symbol:
            result = -result

        return result if -(1<<31) <= result <= (1<<31) - 1 else (1<<31) - 1


if __name__ == "__main__":
    dividend_list = [10, 7, -7, -10, 0, 0, 100, -2147483648]
    divisor_list = [3, -3, 3, -3, -1, 1, 3, -1]

    for dividend, divisor in zip(dividend_list, divisor_list):
        print(Solution().divide(dividend, divisor))
