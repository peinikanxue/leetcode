/*
 * @lc app=leetcode.cn id=318 lang=cpp
 *
 * [318] 最大单词长度乘积
 */
#include <string>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    int maxProduct(vector<string>& words) {
        int ans = 0;
        vector<int> encode_words = encode(words);
        
        for(int i = 0; i < words.size(); ++i){
            for(int j = i + 1; j < words.size(); ++j){
                if((encode_words[i] & encode_words[j]) == 0){
                    ans = max(ans, static_cast<int>(words[i].length() * words[j].length()));
                }
            }
        }

        return ans;
    }

    vector<int> encode(vector<string>& words){
        vector<int> encode_words(words.size(), 0);
        for(int i = 0; i < words.size(); ++i){
            for(const auto &c : words[i]){
                encode_words[i] |= 1 << (c - 'a');
            }
        }

        return encode_words;
    }
};
// @lc code=end

#include<iostream>

int main(int argc, char const *argv[])
{
    vector<string> words {"abcw","baz","foo","bar","xtfn","abcdef"};
    cout << Solution().maxProduct(words) << endl;
    return 0;
}

/*
167/167 cases passed (48 ms)
Your runtime beats 43.1 % of cpp submissions
Your memory usage beats 87.27 % of cpp submissions (15.2 MB)

time: O(L*n + n^2)
space: O(n)

L:为每个词的长度
*/

/*
字母a-z，只有26个，可以被编码到32字节的int中。

然后，判断两个字符串是否有重复，就十分快速了。
*/