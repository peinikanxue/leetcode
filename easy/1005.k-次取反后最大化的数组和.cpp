/*
 * @lc app=leetcode.cn id=1005 lang=cpp
 *
 * [1005] K 次取反后最大化的数组和
 */

#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

// @lc code=start
class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());

        int count_neg = 0, k2;
        for(auto it = nums.begin(); it != nums.end(); ++it){   // 统计负数的数量
            if(*it < 0)
                ++count_neg;
        }

        if(k < count_neg)
            std::transform(nums.begin(), nums.begin() + k, nums.begin(), [](auto x){return -x;});
        else{
            std::transform(nums.begin(), nums.begin() + count_neg, nums.begin(), [](auto x){return -x;});
            k2 = k - count_neg;
            if(k2 % 2){
                auto min_it = min_element(nums.begin(), nums.end());
                *min_it = -*min_it;
            }
        }


        return std::accumulate(nums.begin(), nums.end(), 0);
    }

};
// @lc code=end

/*
80/80 cases passed (4 ms)
Your runtime beats 87.56 % of cpp submissions
Your memory usage beats 26.7 % of cpp submissions (8.9 MB)

time: O(n)
space: O(1)
*/