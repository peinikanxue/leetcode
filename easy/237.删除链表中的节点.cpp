/*
 * @lc app=leetcode.cn id=237 lang=cpp
 *
 * [237] 删除链表中的节点
 */

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// @lc code=start
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* tmp = node->next;
        node->val = node->next->val;
        node->next = node->next->next;
        delete tmp;
    }
};
// @lc code=end


/*
41/41 cases passed (8 ms)
Your runtime beats 89.52 % of cpp submissions
Your memory usage beats 19.62 % of cpp submissions (7.6 MB)

time: O(1)
space: O(1)
*/

/*
题目甚至简单到了，保证不是尾元素
ps:释放空间
*/