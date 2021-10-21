from typing import *


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        change_count = 0
        prefix = False
        for i, y in enumerate(arr[1:]):
            x = arr[i]
            if x == y:
                return False
            if (x - y > 0) != prefix:
                change_count += 1
                prefix = not prefix
        return change_count == 1 and arr[0] - arr[1] < 0


if __name__ == '__main__':
    test_datas = [{'param': [3, 5, 5], 'result': False}]
    for test_list in test_datas:
        print(Solution().validMountainArray([]))
