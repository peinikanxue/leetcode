/*
 * @lc app=leetcode.cn id=187 lang=cpp
 *
 * [187] 重复的DNA序列
 */

#include <iostream>
#include <vector>
#include <map>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> ans;
        map<string, int> record;
        map<string, int>::iterator it;
        if(s.length()<10)
            return ans;
        for(int i=0; i<s.length()-9; ++i){
            string sub_s = s.substr(i, 10);
            it = record.find(sub_s);
            if(it != record.end()){
                if(it->second == 1){    // 不重复
                    ans.push_back(sub_s);
                    record[sub_s]++;
                }
            }
            else{
                record[sub_s] = 1;
            }
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    string s{"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"};
    // string s{"AAAAAAAAAAAAA"};
    // string s{"A"};

    Solution solution = Solution();
    solution.findRepeatedDnaSequences(s);
    return 0;
}

/*
31/31 cases passed (136 ms)
Your runtime beats 14.94 % of cpp submissions
Your memory usage beats 48.04 % of cpp submissions (21.7 MB)

time: O(kn)
space: O(kn)

k:为字串长度。
*/