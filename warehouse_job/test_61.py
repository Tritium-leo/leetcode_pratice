from typing import *
from model.list_node import ListNode


# difficulty = middle
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur_head = head
        for i in range(k):
            loop = cur_head
            while True:
                # 找到倒数第二个
                if loop is None or loop.next is None or loop.next.next is None:
                    break
                loop = loop.next
            # 接上头
            cur_end = loop.next
            # 断开尾
            loop.next = None
            cur_end.next = cur_head
            cur_head = cur_end
        return cur_head


if __name__ == "__main__":
    print(Solution().rotateRight(ListNode.from_list([1, 2, 3, 4, 5]), 2), [4, 5, 1, 2, 3])
