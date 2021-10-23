from typing import *


# difficulty = middle

class Solution:
    def majorityElement1(self, nums: List[int]) -> List[int]:
        # 时间复杂 o(N) ,空间复杂o(N)
        max_count = len(nums) / 3
        code_set = set(nums)
        code_count = {x: nums.count(x) for x in code_set if nums.count(x) > max_count}
        return [k for k, v in code_count]

    def majorityElement(self, nums: List[int]) -> List[int]:
        max_count = len(nums) // 3
        if max_count == 0:
            return list(set(nums))
        nums.sort()
        count = 1
        start = nums.pop(0)
        result = set()
        while nums:
            code = nums.pop(0)
            if code == start:
                count += 1
                if count > max_count:
                    result.add(start)
            else:
                count = 1
                start = code
        return list(result)


if __name__ == '__main__':
    print(list(Solution().majorityElement([3, 2, 3])))
