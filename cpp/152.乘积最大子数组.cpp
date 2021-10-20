/*
 * @lc app=leetcode.cn id=152 lang=cpp
 *
 * [152] 乘积最大子数组
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <limits>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // int max_val = *max_element(nums.begin(), nums.end());
        int max_val = INT32_MIN;    //0x80000000
        int tmp;
        vector<int>::iterator l = nums.begin();
        if(nums.size() == 1)    // 只有一个元素
            return nums[0];
        else if(nums.size() == 0)
            return max_val;
        for(auto r=nums.begin();; ++r){
            if(r == nums.end() || *r == 0){ // 判断顺序反的话，会发生越界访问
                if(l != r && (tmp = sub_max_product(nums, l, r)) > max_val) max_val = tmp;
                l = r+1;
            }

            if(r==nums.end()) break;
        }
        return max_val;
    }

    int sub_max_product(vector<int>& nums, vector<int>::iterator l, vector<int>::iterator r){
        vector<vector<int>::iterator> negative_iters;
        int sub_max_val;
        for(auto it=l; it!=r; ++it){
            if(*it < 0) negative_iters.push_back(it);
        }
        if(r - l == 1 && *l <= 0)   // 只有一个元素，且小于0
            return 0;
        if(negative_iters.size() % 2 == 0){
            sub_max_val = accumulate(l, r, 1, multiplies<int>());
        }else{
            sub_max_val = max(
                accumulate(l, negative_iters.back(), 1, multiplies<int>()), 
                accumulate(negative_iters.front()+1, r, 1, multiplies<int>())
            );
        }
        // cout << *l << ":" << *r << " " << sub_max_val << endl;
        return sub_max_val;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> nums {
        -17, 0, 3, 5, -2, 10, 0, -10, 7, -6, 2, 0, -5, -10, 6, -3, 8, -10, 7, -4, 9, 6, 0, -2, -3, -4
        // 2, 3, -2, 4
        // -2, 0, -1
        // -2
    };
    cout << Solution().maxProduct(nums) << endl;
    return 0;
}

/*
187/187 cases passed (8 ms)
Your runtime beats 35.8 % of cpp submissions
Your memory usage beats 36.99 % of cpp submissions (11.6 MB)

time: O(n)
space: O(n)

空间开销主要是在存储负数的iter，可以优化为O(1)，不过代码没这么简洁。
*/