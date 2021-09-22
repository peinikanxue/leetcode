#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # 先遍历一遍，得到链表长度
        num_len, tmp = 0, head
        while tmp:
            num_len += 1
            tmp = tmp.next
        
        # 计算怎么分配
        alloc_list = [num_len // k] * k     # 平均分配
        last = num_len - num_len // k * k   # 剩余
        for i in range(last):
            alloc_list[i] += 1
        
        # 拆分链表
        ans = []
        for x in alloc_list:
            tail = head
            if tail:
                for _ in range(x-1):
                    tail = tail.next
                ans.append(head)
                head = tail.next
                tail.next = None
            else:
                ans.append(None)
        return ans
# @lc code=end

