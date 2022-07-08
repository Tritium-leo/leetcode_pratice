class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = []
        for code in set(s):
            start_idx = s.index(code)
            end_idx = s.rindex(code)
            ans.append(end_idx - start_idx)
        return (max(ans) if ans else 0) - 1


if __name__ == '__main__':
    print(Solution().maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))
