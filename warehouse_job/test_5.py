class Solution:
    def longestPalindrome1(self, s: str) -> str:
        if len(s) == 1:
            return s
        length_result = {}
        code_count = {}
        for one in s:
            if one not in code_count:
                code_count[one] = 1
            else:
                code_count[one] += 1
        code_count = {k: v for k, v in code_count.items() if v > 1}

        for code, code_num in code_count.items():
            last_start = s.index(code)
            for _ in range(code_num):
                i = s.index(code, last_start)
                last_start = i + 1
                code_count = s.count(code, i) - 1
                if s.count(code) == 0:
                    continue
                max_length = max(length_result) if length_result else 0
                if len(s) - i < max_length:
                    break

                prefix_j = i
                for j in range(code_count):
                    prefix_j = s.index(code, prefix_j + 1)
                    may_str = s[i:prefix_j + 1]
                    if may_str[::-1] == may_str:
                        length_result[len(may_str)] = may_str
        return length_result[max(length_result)] if length_result else s[0]

    # class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        length_result = {}
        for i, code in enumerate(s):
            code_count = s.count(code, i) - 1
            if s.count(code) == 0:
                continue
            # 已找到最长的回文 就结束循环
            max_length = max(length_result) if length_result else 0
            if len(s) - i < max_length:
                break

            prefix_j = i
            for j in range(code_count):
                prefix_j = s.index(code, prefix_j + 1)
                may_str = s[i:prefix_j + 1]
                if may_str[::-1] == may_str:
                    length_result[len(may_str)] = may_str
        return length_result[max(length_result)] if length_result else s[0]


print(Solution().longestPalindrome("aacabdkacaa"))
