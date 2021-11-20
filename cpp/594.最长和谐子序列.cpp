/*
 * @lc app=leetcode.cn id=594 lang=cpp
 *
 * [594] 最长和谐子序列
 */
#include <iostream>
#include <vector>
#include <map>

using namespace std;

// @lc code=start
class Solution {
public:
    int findLHS(vector<int>& nums) {
        int ans = 0;
        map<int, int> counter;
        for(const auto &x : nums){
            ++counter[x];
        }
        bool first_flag = true;
        int pre_k, pre_v;
        for(auto && [k, v] : counter){
            if(first_flag){
                first_flag = false;
            }else if(k - pre_k == 1){
                ans = max(ans, pre_v + v);
            }
            pre_k = k;
            pre_v = v;
        }
        return ans;
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    vector<int> nums {1,3,2,2,5,2,3,7};
    cout << Solution().findLHS(nums) << endl;
    return 0;
}

/*
206/206 cases passed (96 ms)
Your runtime beats 30.96 % of cpp submissions
Your memory usage beats 18.23 % of cpp submissions (40.8 MB)

time: O(n)
space: O(n)
*/