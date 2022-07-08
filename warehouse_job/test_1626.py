from typing import *


# difficulty = simple

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time_keep = [releaseTimes[0]] + [abs(releaseTimes[idx] - releaseTimes[idx + 1]) for idx in
                                         range(len(releaseTimes) - 1)]
        max_time = max(time_keep)
        all_count = time_keep.count(max_time)
        ans = []
        prefix = -1

        for i in range(all_count):
            prefix = time_keep.index(max_time, prefix + 1)
            ans.append(keysPressed[prefix])
        return max(ans)


if __name__ == '__main__':
    print(Solution().slowestKey([9, 29, 49, 50], "cbcd"), ' c')
