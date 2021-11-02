/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;
        sort(intervals.begin(), intervals.end());

        for(auto it=intervals.begin(); it != intervals.end(); ++it){
            if(it == intervals.begin())
            {
                ans.push_back(*it);
                continue;
            }
            if(ans.back()[1] >= (*it)[1]){
                continue;
            }else if(ans.back()[1] >= (*it)[0]){
                ans.back()[1] = (*it)[1];
            }else{
                ans.push_back(*it);
            }
        }

        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution solution;
    vector<vector<int>> intervals;
    intervals.push_back(*(new vector<int>{2, 6}));
    intervals.push_back(*(new vector<int>{1, 3}));
    intervals.push_back(*(new vector<int>{8, 10}));
    intervals.push_back(*(new vector<int>{15, 18}));
    // intervals.push_back(*(new vector<int>{1, 4}));
    // intervals.push_back(*(new vector<int>{4, 5}));

    for(auto x : solution.merge(intervals)){
        cout << x[0] << " " << x[1] << endl;
    }
    return 0;
}

/*
168/168 cases passed (16 ms)
Your runtime beats 86 % of cpp submissions
Your memory usage beats 39.34 % of cpp submissions (13.9 MB)

time: O(n)
space: O(n)
*/
