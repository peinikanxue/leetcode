/*
 * @lc app=leetcode.cn id=264 lang=cpp
 *
 * [264] 丑数 II
 */

#include <vector>

using namespace std;

// @lc code=start
// 题解
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n + 1);
        dp[1] = 1;
        int p2 = 1, p3 = 1, p5 = 1;
        for (int i = 2; i <= n; i++) {
            int num2 = dp[p2] * 2, num3 = dp[p3] * 3, num5 = dp[p5] * 5;
            dp[i] = min(min(num2, num3), num5);
            if (dp[i] == num2) {
                p2++;
            }
            if (dp[i] == num3) {
                p3++;
            }
            if (dp[i] == num5) {
                p5++;
            }
        }
        return dp[n];
    }
};
// @lc code=end


// MD ## 1.
// MD ```c++
// MD #include <vector>
// MD #include <unordered_map>
// MD 
// MD using namespace std;
// MD 
// MD class Solution {
// MD public:
// MD     static unordered_map<int, bool> vis;    // declare
// MD 
// MD     int nthUglyNumber(int n) {
// MD         int i = 0, count = 0;
// MD 
// MD         while(count != n){
// MD             ++i;
// MD             if(isUgly(i)){
// MD                 ++count;
// MD             }
// MD         }
// MD         return i;
// MD     }
// MD 
// MD     bool isUgly(int n){
// MD         static vector<int> factors {2, 3, 5};
// MD         int tmp = n;
// MD         for(int factor : factors){
// MD             while(tmp % factor == 0){
// MD                 tmp /= factor;
// MD                 if(vis.find(tmp) != vis.end()){
// MD                     vis[n] = vis[tmp];
// MD                     return vis[n];
// MD                 }
// MD             }
// MD         }
// MD 
// MD         vis[n] = tmp == 1 ? true : false;
// MD         return vis[n];
// MD     }
// MD };
// MD 
// MD unordered_map<int, bool> Solution::vis; // define
// MD ```


// MD ## 题解
// MD 丑数x丑数=丑数，所以可以通过dp记录，
// MD 然后不断x2,x3,x5，min选出下一个丑数。
// MD 关键在于，维护p1, p2, p3的计数，确定如何正确的推进。
