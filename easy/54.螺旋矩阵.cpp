/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 */
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int direction[][2] {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int pos = 0, r = 0, c = 0;
        int limits[4] {0};  // top, right, bottom, left
        limits[1] = matrix[0].size()-1;
        limits[2] = matrix.size()-1;

        while(limits[0] <= limits[2] && limits[3] <= limits[1]){
            while(limits[0] <= r && r <= limits[2] && limits[3] <= c && c <= limits[1]){
                // cout << r << "," << c << endl;  // debug
                ans.push_back(matrix[r][c]);

                r += direction[pos][0];
                c += direction[pos][1];
            }
            r -= direction[pos][0];
            c -= direction[pos][1];
            limits[pos] += direction[pos][0] == 0 ? direction[pos][1] : -direction[pos][0];    // 边界如何变化可以根据方向确定
            r += direction[pos][0] == 0 ? direction[pos][1] : 0;    // 转移到下一个位置
            c += direction[pos][0] == 0 ? 0 : -direction[pos][0];   // 转移到下一个位置
            pos = (pos + 1) % 4;
        }

        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<vector<int>> matrix;
    matrix.push_back(*(new vector<int>{1,2,3,4}));
    matrix.push_back(*(new vector<int>{5,6,7,8}));
    matrix.push_back(*(new vector<int>{9,10,11,12}));
    Solution solution;
    solution.spiralOrder(matrix);
    return 0;
}

/*
23/23 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 64.26 % of cpp submissions (6.7 MB)

time: O(mn)
space: O(1)

m,n为矩阵的行列数。
*/