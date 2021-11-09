from typing import *
from model.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        loop = head
        while loop.next:
            if loop.next.val == loop.val:
                loop.next = loop.next.next
            else:
                loop = loop.next


print(Solution().deleteDuplicates(ListNode.from_list([1, 1, 2])))
