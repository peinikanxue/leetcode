/*
 * @lc app=leetcode.cn id=397 lang=cpp
 *
 * [397] 整数替换
 */
#include <climits>

// @lc code=start
class Solution {
public:
    int integerReplacement(int n) {
        if(n == INT_MAX)
            return 32;
        int count = 0;

        while(n != 1){
            if(n == 3){
                count += 2;
                break;
            }else if(n % 2 == 0){
                n >>= 1;
            }else{
                n = count1(n - 1) < count1(n + 1) ? n - 1 : n + 1;
            }
            ++count;
        }
        return count;
    }


    int count1(int n){
        int count = 0;
        while(n != 0){
            ++count;
            n = (n - 1) & n;
        }
        return count;
    }

};
// @lc code=end

/*
47/47 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 85.69 % of cpp submissions (5.8 MB)

time: O(1)
space: O(1)

时间和空间的开销不会随输入值的大小发生变化。
*/

/*
/2,-1,+1操作对于二进制操作更加适合，目标就是将二进制的位数减为1，
偶数时，/2操作没有选择，>>1是最好选择，二进制将减少一位
奇数时，-1,+1的选择不会使得二进制的位数减少，为了减少后续出现+1,-1的选择，需要判断+1,-1后的值二进制中'1'的数量更少。

ps:注意n=763的二进制值为1011111011，所以-1,+1后的二进制'1'的个数想同时，优先+1使得连在一起的'1'更多更好，方便一次性'消掉'。
    唯一特殊的是，仅有n=3的二进制值为11，-1,+1后的二进制'1'的个数想同，但却应该-1。
*/

/*
题解
不一定快，但思路更直观，直接。
*/
