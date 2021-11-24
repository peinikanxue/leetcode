/*
 * @lc app=leetcode.cn id=64 lang=cpp
 *
 * [64] 最小路径和
 */

#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        vector<int> dp(grid.front().size(), 0);

        for(int i = 0; i < grid.size(); ++i){
            for(int j = 0; j < dp.size(); ++j){
                if(i == 0 and j == 0)
                    dp[j] = grid[i][j];
                else if(i == 0)
                    dp[j] = dp[j-1] + grid[i][j];
                else if(j == 0)
                    dp[j] = dp[j] + grid[i][j];
                else
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j];
            }
        }

        return dp.back();
    }
};
// @lc code=end\

/*
61/61 cases passed (8 ms)
Your runtime beats 81.31 % of cpp submissions
Your memory usage beats 80.69 % of cpp submissions (9.4 MB)

time: O(mn)
space: O(n)
*/

/*
动态规划
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
*/
