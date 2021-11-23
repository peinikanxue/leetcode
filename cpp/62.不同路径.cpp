/*
 * @lc app=leetcode.cn id=62 lang=cpp
 *
 * [62] 不同路径
 */

#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> counter(n, 1);

        for(int r = 1; r < m; ++r){
            for(int c = 1; c < n; ++c){
                counter[c] += counter[c - 1];
            }
        }

        return counter[n-1];
    }
};
// @lc code=end

#include <iostream>
int main(int argc, char const *argv[])
{
    cout << Solution().uniquePaths(4, 5) << endl;
    return 0;
}

/*
62/62 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 77.94 % of cpp submissions (5.9 MB)

time: O(n^2)
space: O(n)
*/

// MD ![](../imgs/62.svg)

/*
可以递归枚举出每条路径，计数。

但，其实这是有规律的，直接计算即可。
*/