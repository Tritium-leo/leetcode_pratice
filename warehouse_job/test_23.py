from typing import *
from model.list_node import ListNode

# difficulty = hard
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return []
        head = None
        loop = None
        while True:
            min_node = None
            for i in lists:
                if min_node == None:
                    min_node = i
                elif i and min_node.val > i.val:
                    min_node = i
            if min_node is None:
                break
            if head is None:
                head = ListNode(val=min_node.val)
                change_index = lists.index(min_node)
                lists[change_index] = lists[change_index].next
                loop = head
            else:
                loop.next = ListNode(val=min_node.val)
                change_index = lists.index(min_node)
                lists[change_index] = lists[change_index].next
                loop = loop.next
        return head


if __name__ == '__main__':
    input = [ListNode.from_list([1, 4, 5]), ListNode.from_list([1, 3, 4]), ListNode.from_list([2, 6])]
    input = []
    print(Solution().mergeKLists(input))
