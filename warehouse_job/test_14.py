from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        case_item = min(strs, key=lambda x: len(x))
        result = ""
        for i, code in enumerate(case_item):
            strs_check = {True if x[i] == code else False for x in strs}
            if False in strs_check:
                break
            else:
                result += code

        return result


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
