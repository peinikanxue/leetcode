/*
 * @lc app=leetcode.cn id=58 lang=cpp
 *
 * [58] 最后一个单词的长度
 */

#include <iostream>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    int lengthOfLastWord(string s) {
        s = s.erase(s.find_last_not_of(" \n\r\t") + 1);
        return s.length() - 1 - s.find_last_of(" ");
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution solution;
    cout << solution.lengthOfLastWord("   fly me   to   the moon  ") << endl;
    return 0;
}

/*
58/58 cases passed (4 ms)
Your runtime beats 41.19 % of cpp submissions
Your memory usage beats 91.72 % of cpp submissions (6.3 MB)

time: O(n)
space: O(1)
*/