# difficulty = middle

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        the_same_len_2 = 1
        n_len = len(str(n))
        # 找位数一致的2的倍数
        for i in range(n):
            may_2_num = str(2 ** i)
            # 位数过长
            if len(may_2_num) > n_len:
                return False
            # 位数相等 找可能性
            elif len(may_2_num) == n_len:
                may_2_list, n_list = list(may_2_num), list(str(n))
                may_2_list.sort()
                n_list.sort()
                if ''.join(may_2_list) == ''.join(n_list):
                    return True


if __name__ == '__main__':
    print(Solution().reorderedPowerOf2(46))
