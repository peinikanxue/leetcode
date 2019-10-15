#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_head = ListNode(0)
        l3 = l3_head
        
        CF = 0  # 进位标志位
        
        while True:
            if l1 == None and l2 == None and CF == 0:   # 结束条件：两链表都遍历完，并且进位标志为0
                return l3_head.next
            
            # 没有遍历完，建新节点继续
            l3.next = ListNode(0)
            l3 = l3.next
            
            l1_val = l1.val if l1 != None else 0
            l2_val = l2.val if l2 != None else 0
            l3.val = l1_val + l2_val + CF
            
            # 进位处理
            if l3.val >= 10:
                CF = 1
                l3.val %= 10
            else:
                CF = 0
            
            # 遍历链表下一个节点值
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    lx = Solution().addTwoNumbers(l1, l2)
    print(lx.val, ' -> ', lx.next.val, ' -> ', lx.next.next.val)