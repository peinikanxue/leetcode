/*
 * @lc app=leetcode.cn id=263 lang=cpp
 *
 * [263] 丑数
 */

// @lc code=start
class Solution {
public:
    bool isUgly(int n) {
        while(n != 1){
            if(n == 0)
                return false;
            else if(n % 2 == 0)
                n /= 2;
            else if(n % 3 == 0)
                n /= 3;
            else if(n % 5 == 0)
                n /= 5;
            else
                return false;
        }
        return true;
    }
};
// @lc code=end

/*
1013/1013 cases passed (4 ms)
Your runtime beats 47.5 % of cpp submissions
Your memory usage beats 11.98 % of cpp submissions (5.9 MB)

time: O(1)
space: O(1)

能在有限时间内算出。
*/