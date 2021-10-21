from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x, y = None, None
        for x in nums:
            y = target - x
            if x != y:
                if y in nums:
                    break
            elif nums.count(x) >= 2:
                break

        return [nums.index(x), nums.index(y) if x != y else nums.index(y, nums.index(x) + 1)]


if __name__ == '__main__':
    print(Solution().twoSum([2, 3, 5], 5))
