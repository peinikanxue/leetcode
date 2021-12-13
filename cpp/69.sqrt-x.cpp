/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */

#include <iostream>
#include <cmath>

// @lc code=start
// 题解
class Solution {
public:
    int mySqrt(int x) {
        int ans;
        int l = 0, r = x, m;
        while(l <= r){
            m = (l + r) / 2;
            if((long long)m * m <= x){
                ans = m;
                l = m + 1;
            }
            else
                r = m - 1;
        }

        return ans;
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    std::cout << Solution().mySqrt(9) << std::endl;
    return 0;
}

/*
time: O(logx)
space: O(1)
*/

/*
二分法
*/
