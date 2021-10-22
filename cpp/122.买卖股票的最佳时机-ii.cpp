/*
 * @lc app=leetcode.cn id=122 lang=cpp
 *
 * [122] 买卖股票的最佳时机 II
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0, buy = prices[0];
        for(int i=1; i<prices.size(); ++i){
            if(prices[i] > buy)
                ans += prices[i] - buy;
            buy = prices[i];
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> prices {7,1,5,3,6,4};
    cout << Solution().maxProfit(prices) << endl;
    return 0;
}

/*
200/200 cases passed (8 ms)
Your runtime beats 54.78 % of cpp submissions
Your memory usage beats 80 % of cpp submissions (12.6 MB)

time: O(n)
space: O(1)
*/

/*
相比于121题，更加简单，只需要关心相邻2天挣了多少。
*/