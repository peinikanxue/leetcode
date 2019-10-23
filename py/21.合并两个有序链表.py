from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # 边界处理
        if not l1:
            return l2
        elif not l2:
            return l1
        
        # 交换，简化情况
        if l1.val > l2.val:
            l1, l2 = l2, l1

        h1 = l1

        while l1 and l2:
            if l1.val <= l2.val and l1.next and l1.next.val >= l2.val or not l1.next:
                tmp = l2
                l2 = l2.next
                tmp.next = l1.next
                l1.next = tmp
            else:
                l1 = l1.next

        return h1



if __name__ == "__main__":

    l1_vals = [
        [1, 2, 4],
        [2],
    ]

    l2_vals = [
        [1, 3, 4],
        [1],
    ]

    for i in range(len(l1_vals)):
        h1 = l1 = ListNode(0)
        for val in l1_vals[i]:
            l1.next = ListNode(val)
            l1 = l1.next

        h2 = l2 = ListNode(0)
        for val in l2_vals[i]:
            l2.next = ListNode(val)
            l2 = l2.next
    
        h1 = h1.next
        h2 = h2.next

        result = Solution().mergeTwoLists(h1, h2)

        while result.next:
            print(result.val, '->', end='')
            result = result.next
        else:
            print(result.val)
