from typing import *


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = [self.val]
        next_obj = self.next
        while next_obj:
            result.append(next_obj.val)
            next_obj = next_obj.next
        return str(result)

    @staticmethod
    def from_list(l1: List):
        assert len(l1) > 0, 'list mast have one item'
        head = ListNode(l1[0])
        next_link = head
        for one in l1[1:]:
            next_link.next = ListNode(one)
            next_link = next_link.next
        return head
