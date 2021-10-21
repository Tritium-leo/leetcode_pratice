# hard
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        def _inner_func(depth, couples, s, prefix=''):
            level_couple = []
            for index, one in enumerate(s):
                couple = prefix + one
                if couple not in couples:
                    couples.add(couple)
            if depth > 1:
                for couple in level_couple:
                    _inner_func(depth - 1, couples, s[index + 1:], prefix + one)

        couples = set()
        _inner_func(len(s), couples, s)
        return len(couples) % (10 ** 9 + 7)


if __name__ == '__main__':
    test_list = ['abc', 'aba', 'aaa', 'adbae']
    # test_list = ["pcrdhwdxmqdznbenhwjsenjhvulyve"]
    for one in test_list:
        print(one, 'count :', Solution().distinctSubseqII(one))
