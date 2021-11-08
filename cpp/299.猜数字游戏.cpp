/*
 * @lc app=leetcode.cn id=299 lang=cpp
 *
 * [299] 猜数字游戏
 */

#include <iostream>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    string getHint(string secret, string guess) {
        int Bulls = 0, Cows = 0;
        int n = secret.length();
        int secret_count[10]{}; // 计数未使用的数量

        for(int i = 0; i < n; ++i)
            if(secret[i] == guess[i]){
                ++Bulls;
                guess[i] = '.';
            }else{
                ++secret_count[secret[i]-'0'];
            }

        for(int i = 0; i < n; ++i)
            if(guess[i] != '.' and secret_count[guess[i] - '0']-- > 0)
                ++Cows;

        return to_string(Bulls) + "A" + to_string(Cows) + "B";
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    cout << Solution().getHint("1234", "0111") << endl;
    return 0;
}

/*
152/152 cases passed (4 ms)
Your runtime beats 79.4 % of cpp submissions
Your memory usage beats 90.66 % of cpp submissions (6.3 MB)

time: O(n)
space: O(1)
*/