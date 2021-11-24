/*
 * @lc app=leetcode.cn id=66 lang=cpp
 *
 * [66] 加一
 */

#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for(int i = digits.size() - 1; i >= 0; --i){
            if(digits[i] != 9){
                ++digits[i];
                break;
            }else{
                digits[i] = 0;
            }
            if(i == 0)
                digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};
// @lc code=end


/*
111/111 cases passed (4 ms)
Your runtime beats 51.53 % of cpp submissions
Your memory usage beats 94.99 % of cpp submissions (8.3 MB)

time: O(n)
space: O(1)
*/