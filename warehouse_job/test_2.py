from core import *
from typing import *


# Definition for singly-linked list.
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


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1, v2 = l1.val, l2.val
        next_add = 1 if v1 + v2 >= 10 else 0
        result = ListNode((v1 + v2) % 10)
        head = result
        while (l1 and l1.next) or (l2 and l2.next):
            l1, l2 = l1.next if l1 is not None else None, l2.next if l2 is not None else None
            v1, v2 = l1.val if l1 is not None else 0, l2.val if l2 is not None else 0
            result.next = ListNode((v1 + v2 + next_add) % 10)
            result = result.next
            next_add = 1 if v1 + v2 + next_add >= 10 else 0
        if next_add == 1:
            result.next = ListNode(next_add)
        return head


if __name__ == '__main__':
    test_couple = [
        {'param': [(5, 6), (5, 4, 9)], 'result': str([0, 1, 0, 1])},
        {'param': [(2, 4, 3), (5, 6, 4)], 'result': str([7, 0, 8])},
        {'param': [(9, 9, 9, 9, 9, 9, 9), (9, 9, 9, 9)], 'result': str([8, 9, 9, 9, 0, 0, 0, 1])}
    ]
    for test in test_couple:
        p1, p2 = ListNode.from_list(test['param'][0]), ListNode.from_list(test['param'][1])
        result = Solution().addTwoNumbers(p1, p2)
        assert str(result) == test['result'], f'结果错误,Your:{result},Need{test["result"]}'
