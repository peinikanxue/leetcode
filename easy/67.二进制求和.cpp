/*
 * @lc app=leetcode.cn id=67 lang=cpp
 *
 * [67] 二进制求和
 */

#include <iostream>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    string addBinary(string a, string b) {
        if(a.length() < b.length())
            swap(a, b);

        int A, B, C = 0;
        for(int i = 0; i < a.length(); ++i){
            A = a[a.length() - 1 - i] - '0';
            B = i < b.length() ? b[b.length() - 1 - i] - '0' : 0;

            // cout << A << "+" << B << "+" << C << "=" << cal_x(A, B, C) << " C:" << cal_c(A, B, C) << endl;

            a[a.length() - 1 - i] = cal_x(A, B, C) + '0';
            C = cal_c(A, B, C);
        }
        if(C){
            a.insert(0, "1");
        }

        return a;
    }

    int cal_x(int A, int B, int C){
        return A ^ B ^ C;
    }

    int cal_c(int A, int B, int C){
        return ((A ^ B) & C) | (A & B);
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    cout << Solution().addBinary("1010", "11011") << endl;
    cout << Solution().addBinary("1", "111") << endl;
    return 0;
}

/*
294/294 cases passed (4 ms)
Your runtime beats 60.17 % of cpp submissions
Your memory usage beats 80.62 % of cpp submissions (6.1 MB)

time: O(n)
space: O(1)
*/