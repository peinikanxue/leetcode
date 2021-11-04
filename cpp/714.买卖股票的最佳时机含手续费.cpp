/*
 * @lc app=leetcode.cn id=714 lang=cpp
 *
 * [714] 买卖股票的最佳时机含手续费
 */

#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        // 0：不持有，由于今天卖出
        // 1：不持有，由于保持不买
        // 2：持有，由于今天买入
        // 3：持有，由于保存之前的买入状态
        int dp[4]{};
        dp[2] -= prices[0];
        dp[3] -= prices[0];

        for(int i = 1; i < prices.size(); ++i){
            tie(dp[0], dp[1], dp[2], dp[3]) = make_tuple(
                max(dp[2], dp[3]) + prices[i] - fee,        // 可以从持有状态2,3    转为    不持有状态0
                max(dp[0], dp[1]),                          // 可以从不持有状态0,1  维持    不持有状态1
                max(dp[0], dp[1]) - prices[i],              // 可以从不持有状态0,1  转为    持有状态2
                max(dp[2], dp[3])                           // 可以从不持有状态2,3  维持    不持有状态3
            );
        }

        return max(dp[0], dp[1]);
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    vector<int> prices{1, 3, 2, 8, 4, 9};
    cout << Solution().maxProfit(prices, 2) << endl;
    return 0;
}

/*
44/44 cases passed (92 ms)
Your runtime beats 55.1 % of cpp submissions
Your memory usage beats 99.89 % of cpp submissions (53.5 MB)

time: O(n)
space: O(1)
*/

/*
基于309题的思路，可以很容易做出。
*/