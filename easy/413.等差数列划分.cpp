/*
 * @lc app=leetcode.cn id=413 lang=cpp
 *
 * [413] 等差数列划分
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int ans = 0;
        int count, diff_val;

        for(auto it = nums.cbegin(); it != nums.cend(); ++it){
            if(it == nums.cbegin()){            // 第一个元素，需要初始化差值
                if(it + 1 != nums.cend()){
                    count = 1;  // 后面会重复这个，所以初始化为1
                    diff_val = *(it + 1) - *it;
                }
                continue;
            }

            if(*it - *(it-1) == diff_val){
                ++count;
            }else{
                if(count >= 3){
                    // cout << count << endl;
                    ans += _get_combination(count);
                }
                count = 2;  // 重置 (当前元素和前一个元素，共2个，count=2)
                diff_val = *it - *(it-1);
            }

            if(it + 1 == nums.cend() and count >= 3){  // 如果是最后一个元素
                // cout << "end:" << count << endl;
                ans += _get_combination(count);
            }
        }

        return ans;
    }

private:
    /**
     * @brief 计算3个以上相邻的组合数
     */
    int _get_combination(int n, int k=3){
        if(k == n)
            return 1;
        return n - (k - 1) + _get_combination(n, k + 1);
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    // vector<int> nums{1, 2, 3, 4, 7, 10};
    vector<int> nums{1, 2, 3, 8, 9, 10};
    cout << Solution().numberOfArithmeticSlices(nums) << endl;
    return 0;
}

/*
15/15 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 56.66 % of cpp submissions (7.1 MB)

time: O(n)
space: O(1)
*/
