class Solution:
    def reverse(self, x: int) -> int:
        x_reverse = None
        flag = -1 if x < 0 else 1
        x_str = list(str(x)) if x >= 0 else list(str(x)[1:])
        x_str.reverse()
        x_reverse = int(''.join(x_str))
        return flag * x_reverse if -2 ** 31 <= x_reverse <= 2 ** 31 - 1 else 0


if __name__ == "__main__":
    Solution().reverse(-123)
