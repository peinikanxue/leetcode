/*
 * @lc app=leetcode.cn id=476 lang=cpp
 *
 * [476] 数字的补数
 */

#include <iostream>

using namespace std;

// @lc code=start
class Solution {
public:
    int findComplement(int num) {
        int max_bit = 0, ans = 0;
        for(int i=0; i<31; ++i){
            if((num >> i) & 1){
                max_bit = i;
            }
        }
        for(int i=0; i<=max_bit; ++i){
            ans += (!((num >> i) & 1)) << i;
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution solution;
    cout << solution.findComplement(1) << endl;
    return 0;
}

/*
149/149 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 76.21 % of cpp submissions (5.8 MB)

time: O(1)
space: O(1)
*/