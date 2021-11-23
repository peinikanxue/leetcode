/*
 * @lc app=leetcode.cn id=63 lang=cpp
 *
 * [63] 不同路径 II
 */

#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        const int m = obstacleGrid.size(), n = obstacleGrid.front().size();
        vector<int> counter(n, 0);

        for(int c = 0; c < n; ++c){     // init
            if(obstacleGrid[0][c] == 1)
                break;
            counter[c] = 1;
        }

        for(int r = 1; r < m; ++r){
            for(int c = 0; c < n; ++c){
                if(obstacleGrid[r][c] == 1)
                    counter[c] = 0;
                else if(c != 0)
                    counter[c] += counter[c - 1];
            }
        }

        return counter[n-1];
    }
};
// @lc code=end


// MD ## 1.递归枚举
// MD ```c++
// MD class Solution {
// MD public:
// MD     int counter = 0;
// MD     int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
// MD         searchEnd(obstacleGrid, 0, 0);
// MD         return this->counter;
// MD     }
// MD     void searchEnd(vector<vector<int>>& grid, int row, int col){
// MD         if(grid[row][col] == 1)
// MD             return;
// MD         if(row == grid.size() - 1 and col == grid.back().size() - 1){
// MD             ++this->counter;
// MD             return;
// MD         }
// MD         if(row + 1 != grid.size() and grid[row + 1][col] != 1)
// MD             searchEnd(grid, row + 1, col);
// MD         if(col + 1 != grid.back().size() and grid[row][col + 1] != 1)
// MD             searchEnd(grid, row, col + 1);
// MD     }
// MD };
// MD ```
// MD 
// MD Time Limit Exceeded\
// MD 29/41 cases passed (N/A)

// MD ## 2.找规律(动态规划)
// MD 延续62题的思路。\
// MD ps:同62题，只从左上角->右下角，符合单调递增，只用一维数组即可处理。
// MD 
// MD ![](../imgs/63.svg)

/*
41/41 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 86.04 % of cpp submissions (7.4 MB)

time: O(mn)
space: O(n)
*/