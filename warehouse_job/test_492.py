from typing import *


# difficulty = simple

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        result = {}
        for w in range(1, area):
            l = area / w
            if w > l:
                break
            if l == area // w and l >= w:
                result[abs(w - l)] = (int(l), int(w))
        return result[min(result)] if result else [1, 1]


Solution().constructRectangle(1)
