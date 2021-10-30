from typing import *


# difficulty = middle
class Solution:
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backstack(loop_nums, tmp):
            if len(loop_nums) == 0:
                res.add("".join(tmp))
            for idx, i in enumerate(loop_nums):
                backstack(loop_nums[:idx] + loop_nums[idx + 1:], tmp + [str(i)])

        backstack(nums, [])
        return [list(x) for x in res]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        check = [0 for x in range(len(nums))]

        def backstack(tmp):
            if len(tmp) == len(nums):
                res.append(tmp)
            else:
                for i in range(len(nums)):
                    if check[i] == 1:
                        continue
                    if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                        continue
                    check[i] = 1
                    backstack(tmp + [nums[i]])
                    check[i] = 0
        backstack([])
        return res


if __name__ == '__main__':
    print(Solution().permuteUnique([2, 2, 1, 1]))
