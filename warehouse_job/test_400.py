# difficulty = middle
class Solution:
    def findNthDigit(self, n: int) -> int:
        r = 0
        for i in range(len(str(n))):
            add_range = 9 * 10 ** i * (i + 1)
            if add_range + r >= n:
                break
            r += add_range
        code_step = n - r
        next_len = i + 1
        move_step = code_step // next_len + 1 if code_step / next_len != code_step // next_len else code_step // next_len
        # i 几位数 num 第几个
        the_ans = 10 ** i - 1 + move_step
        return int(str(the_ans)[code_step % next_len - 1])


if __name__ == "__main__":
    print(Solution().findNthDigit(9), 9)
    print(Solution().findNthDigit(10), 1)
    print(Solution().findNthDigit(11), 0)
