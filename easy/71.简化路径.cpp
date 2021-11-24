/*
 * @lc app=leetcode.cn id=71 lang=cpp
 *
 * [71] 简化路径
 */

#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

// @lc code=start
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> path_vector;
        deque<string> path_deque;
        string ans;

        split(path, path_vector, "/");

        for(auto it = path_vector.begin(); it != path_vector.end(); ++it){
            if(*it == ".")
                continue;
            else if(*it == ".."){
                if(not path_deque.empty())
                    path_deque.pop_back();
            }
            else
                path_deque.push_back(*it);
        }

        if(path_deque.empty())
            return "/";

        while(not path_deque.empty()){
            ans += "/" + path_deque.front();
            path_deque.pop_front();
        }

        return ans;
    }

    void split(const string s, vector<string>& tokens, const string& sep){
        size_t last_pos = s.find_first_not_of(sep, 0);
        size_t pos = s.find_first_of(sep, last_pos);
        while(string::npos != pos || string::npos != last_pos){
            tokens.push_back(s.substr(last_pos, pos - last_pos));
            last_pos = s.find_first_not_of(sep, pos);
            pos = s.find_first_of(sep, last_pos);
        }
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    cout << Solution().simplifyPath("/a/./b/../../../c/d/") << endl;
    return 0;
}

/*
256/256 cases passed (8 ms)
Your runtime beats 47.17 % of cpp submissions
Your memory usage beats 24.4 % of cpp submissions (9.9 MB)

time: O(n)
space: O(n)
*/
