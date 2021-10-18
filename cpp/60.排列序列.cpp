/*
 * @lc app=leetcode.cn id=60 lang=cpp
 *
 * [60] 排列序列
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    string getPermutation(int n, int k) {
        string ans;
        vector<string> seq;
        for(int i=1; i<=n; i++){
            seq.push_back(to_string(i));
        }

        for(int i=1; i<n; i++){
            int num_prob = factoral(n-i);
            int idx = k / num_prob;
            if(k != 0 && k % num_prob == 0)
                --idx;
            k = num_prob * idx >= k ? 0 : k - num_prob * idx;
            ans += seq[idx];
            seq.erase(seq.begin()+idx);
        }
        ans += seq[0];

        return ans;
    }

    int factoral(int i){
        return i < 2 ? 1 : i * factoral(i-1);
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution solution;
    cout << solution.getPermutation(4, 9) << endl;;
    return 0;
}

/*
200/200 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 7.3 % of cpp submissions (6.1 MB)

time: O(n)
space: O(n)
*/