/*
 * @lc app=leetcode.cn id=73 lang=cpp
 *
 * [73] 矩阵置零
 */

#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<bool> row_t(matrix.size(), false), col_t(matrix[0].size());
        for(int i = 0; i < matrix.size(); ++i){
            for(int j = 0; j < matrix[0].size(); ++j){
                if(matrix[i][j] == 0){
                    row_t[i] = true;
                    col_t[j] = true;
                }
            }
        }
        for(int i = 0; i < matrix.size(); ++i){
            for(int j = 0; j < matrix[0].size(); ++j){
                if(row_t[i] or col_t[j])
                    matrix[i][j] = 0;
            }
        }
    }
};
// @lc code=end

/*
164/164 cases passed (12 ms)
Your runtime beats 77.94 % of cpp submissions
Your memory usage beats 98.43 % of cpp submissions (12.7 MB)

time: O(mn)
space: O(m + n)
*/

/*
记录横纵有0的坐标，放入数组便于查询。
*/
