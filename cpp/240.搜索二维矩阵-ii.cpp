/*
 * @lc app=leetcode.cn id=240 lang=cpp
 *
 * [240] 搜索二维矩阵 II
 */

#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
// 题解
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0, col = matrix[0].size() - 1;
        while(row < matrix.size() and col >= 0){
            if(matrix[row][col] == target)
                return true;
            else if(matrix[row][col] > target)
                --col;
            else
                ++row;
        }

        return false;
    }

};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<vector<int>> matrix{
        {1,4,7,11,15},
        {2,5,8,12,19},
        {3,6,9,16,22},
        {10,13,14,17,24},
        {18,21,23,26,30}
    };
    for(auto x : {1,4,7,11,15,2,5,8,12,19,3,6,9,16,22,10,13,14,17,24,18,21,23,26,30,0,20}){
        cout << x << ":";
        cout << boolalpha << Solution().searchMatrix(matrix, x) << endl;
    }
    return 0;
}

/*
129/129 cases passed (96 ms)
Your runtime beats 72 % of cpp submissions
Your memory usage beats 44.3 % of cpp submissions (14.5 MB)

time: O(m + n)
space: O(1)
*/

/*
之前接触过类似的题，不知道为什么总想着从左上角或者右下角开始。
还总想着使用二分实现O(logn)。
不管横坐标纵坐标都是递增（或者是递减），没办法确定该向那个方向走。

题解从右上角开始，保证了2个方向一个是增，一个是减。
*/