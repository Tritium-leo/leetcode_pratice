from typing import *
from collections import defaultdict


# difficulty = middle
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = defaultdict(int)
        for v in arr:
            res[v] = res[v - difference] + 1
        return max(res.values())


if __name__ == "__main__":
    print(Solution().longestSubsequence([4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8, 8], 0))
