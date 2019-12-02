# 引入验证
from typing import *

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
