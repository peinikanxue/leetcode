/*
 * @lc app=leetcode.cn id=139 lang=cpp
 *
 * [139] 单词拆分
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    bool wordBreak(string s, vector<string>& word_dict) {
        vector<vector<int>> pos_list(s.length());
        this->dp_vis = new vector<bool>(s.length(), false);

        for(int idx = 0; idx < word_dict.size(); ++idx){  // 先预处理，将s每个位置，能从字典查到的词记下，避免每次递归都需要find()
            int pos = -1;
            while((pos = s.find(word_dict[idx], pos + 1)) != -1){
                pos_list[pos].emplace_back(idx);
            }
        }

        _search_word(s, 0, word_dict, pos_list);
        return ans;
    }


private:
    bool ans = false;
    vector<bool> *dp_vis;
    void _search_word(string &s, int pos, vector<string> &word_dict, vector<vector<int>> &pos_list){
        for(auto idx : pos_list[pos]){
            if(this->ans)   // 已经有路径能到达最后的位置，其它的路径都应该直接返回结束。
                return;

            size_t pos_arrive = pos + word_dict[idx].length();
            if(pos_arrive == s.length()){
                ans = true;
            }
            if(pos_arrive < s.length() and not (*this->dp_vis)[pos_arrive]){
                (*this->dp_vis)[pos_arrive] = true;
                _search_word(s, pos + word_dict[idx].length(), word_dict, pos_list);
            }
        }
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    // string s = "catsandog";
    // vector<string> wordDict{"cats", "dog", "sand", "and", "cat"};    // false
    // vector<string> wordDict{"cats", "dog", "sand", "and", "cat", "an"}; // true
    string s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab";   // Time Limit Exceeded
    vector<string> wordDict{"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ab"};
    cout << boolalpha << Solution().wordBreak(s, wordDict) << endl;
    return 0;
}


/*
Accepted
45/45 cases passed (4 ms)
Your runtime beats 93.95 % of cpp submissions
Your memory usage beats 76.71 % of cpp submissions (7.8 MB)

time: O(n^2)
space: O(n)
*/

/*
遍历每个可能的路径。
超时是因为大量的重复，
本题中字典可以重复使用，
而同时其实我们只关心每条路径能到达的最远位置，其它路径如果能到达这个位置，那么就没必要再去遍历，直接跳过即可。
关键在于如何剪枝，跳过重复的路径。

ps:一开始把题想复杂了，以为是匹配完字典；结果应该是匹配完字符串。
*/

// MD ![](../imgs/139.svg)
