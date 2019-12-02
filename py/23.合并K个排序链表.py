from utils import *

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:

#         i = 0
#         while i < len(lists): # 清除空链表
#             if not lists[i]:
#                 lists.remove(lists[i])
#                 continue
#             i += 1

#         if len(lists) == 1:     # 只有一条链表就返回
#             return lists[0]

#         hx = lx = ListNode(0)   # 亚结点

#         while lists:    # lists不为空
#             index = 0
#             p_min = lists[0]
#             for i in range(1, len(lists)):
#                 if lists[i].val < p_min.val:
#                     p_min = lists[i]    # 记录最小的节点
#                     index = i           # 记录索引位置

#             lx.next = lists[index]             # 添加到新链表
#             lx = lx.next
#             lists[index] = lists[index].next   # 向后移
#             while lists[index] and lists[index].val == p_min.val:    # 结点存在的话，遍历完所有相同值的结点
#                 lx.next = lists[index]
#                 lx = lx.next
#                 lists[index] = lists[index].next
#             if lists[index] == None:    # 移除遍历完的链表
#                 lists.remove(lists[index])
            
#             if len(lists) == 1:         # 如果只有一个链表了,剩下的全部接在后面
#                 lx.next = lists[0]
#                 break
        
#         return hx.next

# # 官方题解
# # 分治
# class Solution(object):
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0:
#             return None
#         amount = len(lists)
#         interval = 1
#         while interval < amount:
#             for i in range(0, amount - interval, interval * 2):
#                 lists[i] = self.merge2Lists(lists[i], lists[i + interval])
#             interval *= 2
#         return lists[0] if amount > 0 else lists

#     def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = point = ListNode(0)
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 point.next = l1
#                 l1 = l1.next
#             else:
#                 point.next = l2
#                 l2 = l1
#                 l1 = point.next.next
#             point = point.next
#         if not l1:
#             point.next=l2
#         else:
#             point.next=l1
#         return head.next

# 题解
# 分治 - 递归
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self, l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":

    vals_list = [
        ([1, 4, 5], [1, 3, 4], [2, 6]),
        ([0,1,2],[-10,-8,-5,-4],[],[],[-3],[-10,-9,-6,-4,-3,-2,-2,-1,2],[-9,-9,-2,-1,0,1],[-9,-4,-3,-2,2,2,3,3,4]),
    ]

    for vals in vals_list:
        lists = []
        for val in vals:
            lists.append(util.create_list(val))

        result = Solution().mergeKLists(lists)

        util.print_list(result)
