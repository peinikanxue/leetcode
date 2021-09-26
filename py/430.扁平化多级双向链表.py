#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def enter_child(p):
            while p:
                if p.child:
                    tmp_next = p.next
                    p.child.prev = p
                    p.next = p.child
                    p.child = None
                    last_p = enter_child(p.next)
                    last_p.next = tmp_next
                    if tmp_next:
                        tmp_next.prev = last_p
                if p.next:
                    p = p.next
                else:
                    return p
        enter_child(head)
        return head
        
# @lc code=end

