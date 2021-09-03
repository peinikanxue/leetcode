from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Util:
    '''
        主要方便链表的一些操作
    '''
    def create_linked_list(self, val_list):
        head = li = ListNode(0)
        for val in val_list:
            li.next = ListNode(val)
            li = li.next
        li = head
        head = head.next
        del li
        return head

    def print_linked_list(self, li):
        if not li:
            return
            
        while li.next:
            print(li.val, '-> ', end='')
            li = li.next
        else:
            print(li.val)
util = Util()


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head:    # 边界：没有结点
            return

        p1 = head
        if head.next:   # 如果还有下一个结点
            head = head.next
            p2 = head
        else:           # 边界：只有一个结点
            return head
        # pre = p1
        
        while p1 and p2:
            pre = p1
            p1.next, p2.next = p2.next, p1

            if p1.next: # 如果有下一个结点
                p1 = p1.next
                p2 = p1.next
                if p2:  # 如果还有p2，将之前的p1指向当前的p2
                    pre.next = p2
            else:
                p1 = None
            
        return head


if __name__ == "__main__":
    
    val_list = [
        [],
        [1, 2, 3],
        [1, 2, 3, 4],
    ]

    for val in val_list:
        l = util.create_linked_list(val)
        result = Solution().swapPairs(l)
        util.print_linked_list(result)
