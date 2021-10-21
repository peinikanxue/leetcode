/*
 * @lc app=leetcode.cn id=1567 lang=cpp
 *
 * [1567] 乘积为正数的最长子数组长度
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        if(nums.size() < 1)
            return 0x80000000;
        int max_val = nums[0]>0 ? 1 : 0, min_val = nums[0]<0 ? -1 : 0;
        int ans = max_val;

        for(int i=1; i<nums.size(); ++i){
            int x = nums[i] == 0 ? 0 : (nums[i] > 0 ? 1 : -1);
            int mx = max_val, mn = min_val;
            max_val = max(x*mx>0 ? mx+1: 0, max(x*mn>0 ? -mn+1: 0, x>0 ? 1: 0));
            min_val = min(x*mn<0 ? mn-1: 0, min(x*mx<0 ? -mx-1: 0, x<0 ? -1: 0));
            // cout << max_val << "\t" << min_val << endl;
            ans = max(max_val, ans);
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> nums {-17, 0, 3, 5, -2, 10, 0, -10, 7, -6, 2, 0, -5, -10, 6, -3, 8, -10, 7, -4, 9, 6, 0, -2, -3, -4};
    cout << Solution().getMaxLen(nums) << endl;
    return 0;
}

/*
112/112 cases passed (72 ms)
Your runtime beats 99.35 % of cpp submissions
Your memory usage beats 95.09 % of cpp submissions (56.4 MB)

time: O(n)
space: O(1)
*/

/*
同152题乘积最大子数组。
本题不关心值大小，只在意正负，所以将乘积改为计数。
并且正负分开计数。
*/