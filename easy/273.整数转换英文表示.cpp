/*
 * @lc app=leetcode.cn id=273 lang=cpp
 *
 * [273] 整数转换英文表示
 */

#include <iostream>
#include <string>
#include <map>

using namespace std;

// @lc code=start
class Solution {
public:
    map<int, string> dict {
        // {0, "Zero"},
        {1, "One"},
        {2, "Two"},
        {3, "Three"},
        {4, "Four"},
        {5, "Five"},
        {6, "Six"},
        {7, "Seven"},
        {8, "Eight"},
        {9, "Nine"},
        {10, "Ten"},
        {11, "Eleven"},
        {12, "Twelve"},
        {13, "Thirteen"},
        {14, "Fourteen"},
        {15, "Fifteen"},
        {16, "Sixteen"},
        {17, "Seventeen"},
        {18, "Eighteen"},
        {19, "Nineteen"},
        {20, "Twenty"},
        {30, "Thirty"},
        {40, "Forty"},
        {50, "Fifty"},
        {60, "Sixty"},
        {70, "Seventy"},
        {80, "Eighty"},
        {90, "Ninety"},
        {100, "Hundred"},  // one hundred 百
        // {1000, "Thousand"}, // 千
        // {1000000, "Million"}, // 百万
        // {1000000000, "Billion"}, // 十亿
    };
    
    string numberToWords(int num) {
        string ans, sub_ans;
        string ranks[] = {"", "Thousand", "Million", "Billion"};
        int tmp, rank=0;
        
        if(num == 0)
            return "Zero";
        
        // 判断位数
        while(num){
            tmp = num % 1000;
            num /= 1000;
            if((sub_ans = numberToWords3(tmp)) != "")
                ans = sub_ans + ranks[rank] + " " + ans;
            ++rank;
        }
        ans = ans.erase(ans.find_last_not_of(" \n\r\t")+1);

        return ans;
    }

    string numberToWords3(int num){
        string ans;
        if(num >= 100){
            ans += dict[num/100];
            ans += " ";
            ans += dict[100];
            ans += " ";
            num = num - num/100*100;
        }
        if(num >= 20){
            ans += dict[num/10*10];
            ans += " ";
            if(num%10 != 0){
                ans += dict[num%10];
                ans += " ";
            }
        }else{
            if(num != 0){
                ans += dict[num];
                ans += " ";
            }
        }
        return ans;
    }
};
// @lc code=end


int main(int argc, char const *argv[])
{
    Solution solution;
    cout << solution.numberToWords(123) << endl;
    cout << solution.numberToWords(112) << endl;
    cout << solution.numberToWords(120) << endl;
    cout << solution.numberToWords(100) << endl;
    cout << solution.numberToWords(200) << endl;
    cout << solution.numberToWords(0) << endl;
    cout << solution.numberToWords(10) << endl;
    cout << solution.numberToWords(12) << endl;
    cout << solution.numberToWords(20) << endl;
    cout << solution.numberToWords(27) << endl;
    cout << solution.numberToWords(12345) << endl;
    cout << solution.numberToWords(332345) << endl;
    cout << solution.numberToWords(1234567) << endl;
    cout << solution.numberToWords(1234567891) << endl;
    cout << solution.numberToWords(1000000) << endl;
    return 0;
}

/*
601/601 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 6.59 % of cpp submissions (8.2 MB)

time: O(1)
space: O(1)

空间开销为固定的翻译字典
*/

/*
简单题，观察规律，三个数为一组处理，拆分成子问题。
*/