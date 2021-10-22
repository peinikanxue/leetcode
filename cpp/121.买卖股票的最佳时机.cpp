/*
 * @lc app=leetcode.cn id=121 lang=cpp
 *
 * [121] 买卖股票的最佳时机
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = prices[0], max_val = 0;
        for(int i=1; i<prices.size(); ++i){
            max_val = max(max_val, prices[i]-l);
            l = min(l, prices[i]);
        }
        return max_val;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> prices {7, 2, 5, 3, 1, 6, 4};
    cout << Solution().maxProfit(prices) << endl;
    return 0;
}


/*
211/211 cases passed (100 ms)
Your runtime beats 78.26 % of cpp submissions
Your memory usage beats 62.39 % of cpp submissions (91.1 MB)

time: O(n)
space: O(1)
*/

/*
扫描，得到当前元素与记录的最小元素之差，记录最大的差。
*/