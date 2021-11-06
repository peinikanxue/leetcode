/*
 * @lc app=leetcode.cn id=1218 lang=cpp
 *
 * [1218] 最长定差子序列
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// @lc code=start
// 题解
class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int, int> dp;
        int ans = 1;

        for(const int &x : arr){
            dp[x] = dp[x - difference] + 1;
            ans = max(ans, dp[x]);
        }
        return ans;
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    vector<int> arr {1,5,7,8,5,3,4,2,1};
    cout << Solution().longestSubsequence(arr, -2) << endl;
    return 0;
}

/*
39/39 cases passed (120 ms)
Your runtime beats 48.99 % of cpp submissions
Your memory usage beats 30.3 % of cpp submissions (55.3 MB)

time: O(n)
space: O(n)
*/

/*
扫描每个元素，只关心 (当前元素 - difference) 之前存在就计数。
*/