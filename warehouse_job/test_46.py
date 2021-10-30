from typing import *


# difficulty = middle
class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(loop_nums, tmp):
            if len(loop_nums) == 0:
                res.append(tmp)
            for idx, v in enumerate(loop_nums):
                backtrack(loop_nums[:idx] + loop_nums[idx + 1:], tmp + [v])

        backtrack(nums, [])
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        check = [0 for x in range(len(nums))]

        def backtrack(tmp):
            if len(tmp) == len(nums):
                res.append(tmp)
            for i in range(len(nums)):
                if check[i]:
                    continue
                check[i] = 1
                backtrack(tmp + [nums[i]])
                check[i] = 0

        backtrack([])
        return res


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
