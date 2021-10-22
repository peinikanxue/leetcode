/*
 * @lc app=leetcode.cn id=1014 lang=cpp
 *
 * [1014] 最佳观光组合
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        vector<int> dp(values.size());

        for(int i=0; i<values.size(); ++i){
            dp[i] += values[i];
            for(int k=1; k<values[i] && i+k<values.size(); ++k){
                // dp[i+k] = max(dp[i+k], values[i]-k);
                if(values[i]-k > dp[i+k])
                    dp[i+k] = values[i]-k;
                else                    //剪枝
                    break;
            }
        }

        return *max_element(dp.begin(), dp.end());
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> values {6, 1, 5, 2, 6, 1, 2, 7};
    cout << Solution().maxScoreSightseeingPair(values) << endl;
    return 0;
}

/*
53/53 cases passed (180 ms)
Your runtime beats 6.78 % of cpp submissions
Your memory usage beats 11.19 % of cpp submissions (39.9 MB)

time: O(nlogn)
space: O(n)
*/

/*
题解比较巧妙，
将值拆分为2部分，2部分值都是固定（并不是指数组的值为同一个固定数，而是数组内的数不会随着遍历发生变化），
确定状态的转移，值的影响范围mx，
求出最大的和。

time: O(n)
space: O(1)
*/