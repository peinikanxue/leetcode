from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

#         nodes = []
#         node = ListNode(0)  # 在前面加一个节点便于操作
#         node.next = head
#         new_head = node

#         while node.next:
#             nodes.append(node)
#             node = node.next
#         else:
#             nodes.append(node)
        
#         if n == 1:  # 边界情况
#             nodes[-2].next = None
#         elif len(nodes) < 3:    # 边界情况
#             nodes[-n-1].next = None
#         elif nodes[-n].next:
#             nodes[-n-1].next = nodes[-n+1]

#         return new_head.next


# 题解
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        new_head = p1 = p2 = ListNode(0)
        p1.next = head

        while n+1:
            p1 = p1.next
            n -= 1
        
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next

        return new_head.next


if __name__ == "__main__":
    vals = [
        [1, 2, 3, 4, 5],
        [1],
        [1, 2],
        [1, 2],
    ]
    n_list = [2, 1, 2, 1]

    for i in range(len(vals)):
        head = None
        is_frist = True
        for val in vals[i]:
            if is_frist:
                head = node = ListNode(val)
                is_frist = False
                continue
            node.next = ListNode(val)
            node = node.next

        result = Solution().removeNthFromEnd(head, n_list[i])
        if result:
            while result.next:
                print(result.val, ' -> ', end='')
                result = result.next
            else:
                print(result.val)
