/*
 * @lc app=leetcode.cn id=91 lang=cpp
 *
 * [91] 解码方法
 */

#include <string>

using namespace std;

// @lc code=start
// 题解
class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0') return 0;
        int pre = 1, curr = 1;//dp[-1] = dp[0] = 1
        for (int i = 1; i < s.size(); i++) {
            int tmp = curr;
            if (s[i] == '0')
                if (s[i - 1] == '1' || s[i - 1] == '2') curr = pre;                         // 跳1步
                else return 0;                                                              // 不能跳
            else if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] >= '1' && s[i] <= '6'))    // 跳2步
                curr = curr + pre;
            pre = tmp;
        }
        return curr;
    }
};
// @lc code=end

/*
可能的路径数计算有问题，不应该是 2位数能满足0<s.substr[i-1, 2]<26，路径+1；
而是类似类似91题跳阶梯，能组成满足条件的2位数時，路径数是dp[i-2]+dp[i-1]。
*/

// MD ![](https://pic.leetcode-cn.com/c09dc70d3085792b2b8417843e297f6841fd12f921b0e4fe28a2c4a8dc86dd1e-image.png)
