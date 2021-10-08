/*
 * @lc app=leetcode.cn id=118 lang=cpp
 *
 * [118] 杨辉三角
 */

#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        ans.push_back(vector<int>{1});

        for(int i = 1; i < numRows; ++i){
            vector<int> row {1, 1};
            vector<int> &pre = ans.back();
            for(int j = 1; j < i; ++j){
                row.insert(row.begin()+j, pre[j-1] + pre[j]);
                // cout << i << " " << j << ":" << pre[j-1] << "+" << pre[j] << endl;  // debug
            }
            ans.push_back(row);
        }

        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    vector<vector<int>> ans = s.generate(5);

    for(auto li : ans){
        for(auto x : li){
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}

