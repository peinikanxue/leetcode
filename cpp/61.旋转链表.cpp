/*
 * @lc app=leetcode.cn id=61 lang=cpp
 *
 * [61] 旋转链表
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <tuple>

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr){
            return head;
        }

        int count;
        ListNode* tail;
        std::tie(count, tail) = countNodeAndGetTail(head);

        count = count - k % count - 1;

        ListNode* tmp = head;
        while(count--)
            tmp = tmp->next;
        
        tail->next = head;
        head = tmp->next;
        tmp->next = nullptr;

        return head;
    }

    std::tuple<int, ListNode*> countNodeAndGetTail(ListNode* head){
        int count = 0;
        ListNode* tail = nullptr;
        while(head){
            ++count;
            if(head->next == nullptr)
                tail = head;
            head = head->next;
        }
        return std::make_tuple(count, tail);
    }
};
// @lc code=end

#include<iostream>

int main(int argc, char const *argv[])
{
    ListNode head(1);
    ListNode node2(2);
    ListNode node3(3);
    ListNode node4(4);
    ListNode node5(5);
    ListNode node6(6);
    head.next = &node2;
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node5;
    node5.next = &node6;

    ListNode* tmp = Solution().rotateRight(&head, 5);

    while(tmp){
        std::cout << tmp->val << std::endl;
        tmp = tmp->next;
    }
    return 0;
}

/*
231/231 cases passed (4 ms)
Your runtime beats 93.95 % of cpp submissions
Your memory usage beats 19.21 % of cpp submissions (11.5 MB)

time: O(n)
space: O(1)
*/