/*
 * @lc app=leetcode.cn id=412 lang=cpp
 *
 * [412] Fizz Buzz
 */

#include <vector>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector <string> ans;
        for(int i=1; i<=n; ++i){
            if(i%3==0 && i%5==0)
                ans.push_back("FizzBuzz");
            else if(i % 3 == 0)
                ans.push_back("Fizz");
            else if(i % 5 == 0)
                ans.push_back("Buzz");
            else
                ans.push_back(to_string(i));
        }
        return ans;
    }
};
// @lc code=end

/*
8/8 cases passed (4 ms)
Your runtime beats 82.41 % of cpp submissions
Your memory usage beats 71.92 % of cpp submissions (7.7 MB)

time: O(1)
space: O(1)
*/