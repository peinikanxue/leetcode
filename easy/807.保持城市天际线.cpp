/*
 * @lc app=leetcode.cn id=807 lang=cpp
 *
 * [807] 保持城市天际线
 */

#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> row_max, col_max;
        int ans = 0;

        // 获取行列的最大值
        for(const vector<int> &row : grid){
            row_max.push_back(*std::max_element(row.cbegin(), row.cend()));
        }
        for(int j = 0; j < grid[0].size(); ++j){
            int tmp = 0;
            for(int i = 0; i < grid.size(); ++i){
                tmp = max(tmp, grid[i][j]);
            }
            col_max.push_back(tmp);
        }

        // 计算差值
        for(int i = 0; i < grid.size(); ++i){
            for(int j = 0; j < grid[0].size(); ++j){
                ans += min(row_max[i], col_max[j]) - grid[i][j];
            }
        }

        return ans;
    }
};
// @lc code=end

/*
133/133 cases passed (4 ms)
Your runtime beats 96.23 % of cpp submissions
Your memory usage beats 24.8 % of cpp submissions (9.9 MB)

time: O(n^2)
space: O(n)
*/