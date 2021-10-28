/*
 * @lc app=leetcode.cn id=496 lang=cpp
 *
 * [496] 下一个更大元素 I
 */

#include <vector>
#include <map>
#include <stack>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        map<int, int> dict;
        stack<int> my_stack;
        for(int i = 0; i < nums2.size(); ++i)
            dict.emplace(nums2[i], -1);
        for(auto it = nums2.rbegin(); it != nums2.rend(); ++it){
            if(not my_stack.empty() and my_stack.top() > *it)
                dict[*it] = my_stack.top();
            else{
                while(not my_stack.empty() and my_stack.top() < *it)
                    my_stack.pop();
                dict[*it] = my_stack.empty() ? -1 : my_stack.top();
            }
            my_stack.push(*it);
        }

        for(auto x : nums1){
            ans.push_back(dict[x]);
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> nums1{1,3,5,2,4};
    vector<int> nums2{6,5,2,4,1,7,3,8};
    Solution().nextGreaterElement(nums1, nums2);
    return 0;
}

/*
15/15 cases passed (4 ms)
Your runtime beats 92.58 % of cpp submissions
Your memory usage beats 5.05 % of cpp submissions (8.9 MB)

time: O(m+n)
space: O(m+n)
*/

/*
从右向左遍历，使用栈记录较大的元素，并将该元素赋给nums2的字典。
*/