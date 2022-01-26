/*
 * @lc app=leetcode.cn id=65 lang=cpp
 *
 * [65] 有效数字
 */

#include <string>
#include <regex>

using namespace std;

// @lc code=start
class Solution {
public:
    static const std::regex num_pattern;    //? 题解-评论，声明为静态，避免反复构造。否则超时。
    bool isNumber(string s) {
        if(std::regex_match(s, num_pattern))
            return true;
        return false;
    }
};

const std::regex Solution::num_pattern("[-+]?((\\d+\\.?\\d*)|(\\.?\\d+))([eE][-+]?\\d+)?");  // [-+]?((\d+\.?\d*)|(\.?\d+))([eE][-+]?\d+)?
// @lc code=end

#include <iostream>
#include <ctime>

int main(int argc, char const *argv[])
{
    auto t1 = clock();
    cout << boolalpha << Solution().isNumber("-94.740e-7") << noboolalpha << endl;
    cout << (clock() - t1) / static_cast<float>(CLOCKS_PER_SEC) << "s" << endl;
    cout << CLOCKS_PER_SEC << endl;
    return 0;
}

/*
1488/1488 cases passed (8 ms)
Your runtime beats 29.47 % of cpp submissions
Your memory usage beats 18.81 % of cpp submissions (9.5 MB)
*/

// TODO DFA实现
