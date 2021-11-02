/*
 * @lc app=leetcode.cn id=119 lang=cpp
 *
 * [119] 杨辉三角 II
 */

#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans;
        ans.push_back(1);

        for(int i = 1; i < rowIndex+1; ++i){
            for(int j = i-1; j > 0; --j){
                ans[j] = ans[j-1] + ans[j];
            }
            ans.push_back(1);

            // for(auto x : ans){
            //     cout << x << " ";
            // }
            // cout << endl;
        }

        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    vector<int> ans = s.getRow(5);

    for(auto x : ans){
        cout << x << " ";
    }
    cout << endl;
    return 0;
}