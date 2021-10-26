/*
 * @lc app=leetcode.cn id=309 lang=cpp
 *
 * [309] 最佳买卖股票时机含冷冻期
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
// 题解
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {

        vector<vector<int>> dp(prices.size(), vector<int>(4));
        dp[0][0] = 0;               // 不持有股票，之前就不持有，继续保持；
        dp[0][1] = 0;               // 不持有股票，由于卖出去了（冷冻）；
        dp[0][2] = -1 * prices[0];  // 持有股票，今天买入的；
        dp[0][3] = -1 * prices[0];  // 持有股票，非今天买入的，继续保持；
        for (int i = 1; i < prices.size(); i++)
        {
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]);                 // 前一天不持有股票的两种情况的最大值
            dp[i][1] = max(dp[i - 1][2], dp[i - 1][3]) + prices[i];     // 今天卖出股票，前一天持有股票的最大值+prices[i]
            dp[i][2] = dp[i - 1][0] - prices[i];                        // 今天买入股票，前一天一定没有卖出股票
            dp[i][3] = max(dp[i - 1][2], dp[i - 1][3]);                 // 今天没买股票，却持有股票，是前一天继承来的,有两种情况
        }

        return max(dp[prices.size() - 1][0], dp[prices.size() - 1][1]);
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> prices{
        // 7, 1, 4, 2, 5, 2, 4, 5, 1, 6, 4
        6, 1, 3, 2, 4, 7};
    cout << Solution().maxProfit(prices) << endl;
    return 0;
}

/*
time: O(n)
space: O(n) （可以轻易优化到O(1)）
*/