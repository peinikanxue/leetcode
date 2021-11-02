/*
 * @lc app=leetcode.cn id=57 lang=cpp
 *
 * [57] 插入区间
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>>::iterator it_l = intervals.end(), it_r = intervals.end();

        for(auto it = intervals.begin(); it != intervals.end(); ++it){
            if(it == intervals.begin() && newInterval[1] < (*it)[0]){   // 首
                // cout << "首" << (*it)[0] << endl;           // debug
                intervals.emplace(it, newInterval);
                return intervals;
            }
            if((*it)[1] < newInterval[0] && (it+1) != intervals.end() && (*(it+1))[0] > newInterval[1]){    // 插入
                // cout << "插入" << (*it)[0] << endl;         // debug
                intervals.emplace(it+1, newInterval);
                return intervals;
            }
            if(newInterval[0] <= (*it)[0]){ // 左边界[
                // cout << "左边界[" << (*it)[0] << endl;          // debug
                it_l = it;
                break;
            }
            if((*it)[0] <= newInterval[0] && newInterval[0] <= (*it)[1]){    // [左边界]
                // cout << "[左边界]" << (*it)[0] << endl;         // debug
                it_l = it;
                break;
            }
        }
        for(auto it = intervals.end(); it != intervals.begin(); --it){
            if(it_l != intervals.end() && newInterval[1] >= (*(it-1))[1]){  // ]右边界
                // cout << "]右边界" << (*(it-1))[0] << endl;          // debug
                it_r = it-1;
                (*it_l)[1] = newInterval[1];
                if(newInterval[0] <= (*it_l)[0])
                    (*it_l)[0] = newInterval[0];
                intervals.erase(it_l+1, it_r+1);
                return intervals;
            }
            if(it_l != intervals.end() && (*(it-1))[0] <= newInterval[1] && newInterval[1] <= (*(it-1))[1]){    // [右边界]
                // cout << "[右边界]" << (*(it-1))[0] << endl;         // debug
                it_r = it-1;
                (*it_l)[1] = (*(it-1))[1];
                if(newInterval[0] <= (*it_l)[0])
                    (*it_l)[0] = newInterval[0];
                intervals.erase(it_l+1, it_r+1);
                return intervals;
            }
        }

        // cout << "尾" << endl;           // debug
        intervals.push_back(newInterval);   // 尾

        return intervals;
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    Solution solution;
    vector<vector<int>> intervals {
        // {2, 4}, {7, 9}, {12, 13}

        // {4, 6}

        //

    };
    vector<int> newIntervals = {
        // 0, 1
        // 5, 6
        // 10, 11
        // 15, 17
        // 1, 2
        // 4, 5
        // 5, 7
        // 9, 10
        // 10, 12
        // 13, 15
        // 1, 3
        // 3, 5
        // 3, 8
        // 1, 11
        // 1, 12
        // 5, 11
        // 8, 15
        // 0, 17

        2, 3
    };

    solution.insert(intervals, newIntervals);

    for(auto it : intervals){
        cout << it[0] << "-" << it[1] << " ";
    }
    cout << endl;
    return 0;
}

/*
156/156 cases passed (12 ms)
Your runtime beats 88.76 % of cpp submissions
Your memory usage beats 37.08 % of cpp submissions (16.7 MB)

time: O(n)
space: O(1)
*/