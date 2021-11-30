/*
 * @lc app=leetcode.cn id=400 lang=cpp
 *
 * [400] 第 N 位数字
 */

#include <cmath>
#include <string>

// @lc code=start
class Solution {
public:
    int findNthDigit(int n) {
        int m = 1, num_range_str, idx, num;
        while (m < 9 and n > (num_range_str = m * 9 * pow(10, m - 1)))  // m >= 9时，num_range_str超过INT_MAX
        {
            n = n - num_range_str;
            ++m;
        }

        idx = n % m;
        num = n / m + (pow(10, m - 1) - 1) + (idx == 0 ? 0 : 1);    // 该范围的第几个数 + 处于那个范围 + 是否前进一个数

        if(idx)
            return std::to_string(num)[idx-1] - '0';                // idx != 0, 是数字的idx-1位
        else
            return std::to_string(num)[m-1] - '0';                  // idx == 0, 是数字的最后一位数
    }
};
// @lc code=end

#include <iostream>

int main(int argc, char const *argv[])
{
    std::cout << Solution().findNthDigit(1234) << std::endl;
    // std::cout << Solution().findNthDigit(1000000000) << std::endl;
    return 0;
}

/*
71/71 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 37.24 % of cpp submissions (5.9 MB)

time: O(1)
space: O(1)

在确定时间内可完成。
*/

// MD ![](../imgs/400.svg)
