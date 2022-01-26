/*
 * @lc app=leetcode.cn id=74 lang=cpp
 *
 * [74] 搜索二维矩阵
 */

#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0, col = matrix[0].size() - 1;
        while(row < matrix.size() and col >= 0){
            if(matrix[row][col] == target)
                return true;
            else if(matrix[row][col] < target)
                ++row;
            else
                --col;
        }
        return false;
    }
};
// @lc code=end

/*
133/133 cases passed (4 ms)
Your runtime beats 76.62 % of cpp submissions
Your memory usage beats 99.53 % of cpp submissions (9 MB)

time: O(m + n)
space: O(1)
*/

/*
递增2维矩阵，选择一个角作为起始点，保证x,y方向要么增/要么减。
*/
