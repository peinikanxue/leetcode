/*
 * @lc app=leetcode.cn id=709 lang=cpp
 *
 * [709] 转换成小写字母
 */

#include <string>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    string toLowerCase(string s) {
        transform(s.begin(), s.end(), s.begin(), [](int c){return 'A' <= c and c <= 'Z' ? c + 32 : c;});
        return s;
    }
};
// @lc code=end

/*
114/114 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 70.94 % of cpp submissions (6 MB)

time: O(n)
space: O(1)
*/
