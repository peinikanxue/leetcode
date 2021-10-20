/*
 * @lc app=leetcode.cn id=1143 lang=cpp
 *
 * [1143] 最长公共子序列
 */

#include <iostream>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int dp[text1.length()+1][text2.length()+1];

        for(int i=0; i<=text1.length(); ++i)
            for(int j=0; j<=text2.length(); ++j)
                if(i == 0 || j == 0)
                    dp[i][j] = 0;

        for(int i=1; i<=text1.length(); ++i){
            for(int j=1; j<=text2.length(); ++j){
                if(text1[i-1] == text2[j-1])
                    dp[i][j] = max(dp[i-1][j-1]+1, max(dp[i-1][j], dp[i][j-1]));
                else
                    dp[i][j] = max(dp[i-1][j-1], max(dp[i-1][j], dp[i][j-1]));
            }
        }
        return dp[text1.length()][text2.length()];
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    cout << Solution().longestCommonSubsequence("abcde", "ace") << endl;;
    return 0;
}

/*
44/44 cases passed (4 ms)
Your runtime beats 99.98 % of cpp submissions
Your memory usage beats 89.19 % of cpp submissions (10.5 MB)

time: O(mn)
space: O(mn)

m,n分别为两字符串的长度。
*/

/*
动态规划
同583题
*/