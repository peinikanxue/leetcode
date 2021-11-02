/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 */

#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans;
        int count = 1;
        int direction[][2] {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int pos = 0, r = 0, c = 0;
        int limits[4] {0, n-1, n-1, 0};  // top, right, bottom, left
        
        // init ans
        for(int i=0; i<n; i++){
            ans.push_back(*(new vector<int>));
            // for(int j=0; j<n; j++){
            //     ans[i].push_back(0);
            // }
            ans[i].resize(n);
        }

        // 赋值
        while(limits[0] <= limits[2] && limits[3] <= limits[1]){
            while(limits[0] <= r && r <= limits[2] && limits[3] <= c && c <= limits[1]){
                ans[r][c] = count++;

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
    Solution solution;
    solution.generateMatrix(3);
    return 0;
}

/*
20/20 cases passed (4 ms)
Your runtime beats 33.94 % of cpp submissions
Your memory usage beats 81.85 % of cpp submissions (6.4 MB)

time: O(mn)
space: O(1)
*/

/*
同54题
*/