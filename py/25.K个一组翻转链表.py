from utils import *

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if not head:    # 边界：没有节点
            return

        p1 = p2 = new_head = p_next = head
        count = k - 1

        while count and new_head.next:    # 计数，看看后面的节点是否还够翻转
            count -= 1
            new_head = new_head.next
        
        if count == 0:  # 可以翻转
            p_next = new_head.next
            p2 = p1.next

            while p1 != new_head:   # 交换这k个节点
                p_tmp = p2.next
                p2.next = p1
                p1 = p2
                p2 = p_tmp
            
            head.next = self.reverseKGroup(p_next, k)   # 迭代后面的节点
        else:
            new_head = head
        
        return new_head


if __name__ == "__main__":
    
    val_list = [
        [],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    k_list = [1, 2, 3, 7]

    for val, k in zip(val_list, k_list):
        l = util.create_linked_list(val)
        result = Solution().reverseKGroup(l, k)
        util.print_linked_list(result)