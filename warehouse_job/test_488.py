from utils.timer import timer
import re


# difficulty = hard
class Solution:
    # @timer
    def findMinStep(self, board: str, hand: str) -> int:
        hand = ''.join(sorted(list(hand)))
        res = []
        all_str = board + hand
        if all_str.count('R') == 2 or all_str.count('Y') == 2 or all_str.count('B') == 2 or all_str.count(
                'G') == 2 or all_str.count('W') == 2:
            return -1

        def backstack(_board, _hand, tmp):
            if _board == "" or _hand == "":
                if _board == "":
                    res.append(len(tmp))
                return
            for i in range(len(_board)):
                for j in range(len(_hand)):
                    # 相同颜色只放置最后一个
                    if i > 0 and _board[i - 1] == _hand[j]:
                        continue
                    # 手里颜色相同不重复放置
                    if j > 0 and _hand[j] == _hand[j - 1]:
                        continue
                    # 第 3 个剪枝条件: 只考虑放置新球后有可能得到更优解的位置
                    #  - 第 1 种情况 : 当前球颜色与后面的球的颜色相同
                    #  - 第 2 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
                    # choose = True
                    choose = False
                    if 0 < i < len(_board) and _board[i - 1] == _board[i] and _board[i - 1] != _hand[j]:
                        choose = True
                    if i < len(_board) and _board[i] == _hand[j]:
                        choose = True
                    if choose:
                        _board_loop = _board[:i] + _hand[j] + _board[i:]
                        _board_loop = self.resolve_str(_board_loop)
                        backstack(_board_loop, _hand[:j] + _hand[j + 1:], tmp + [_hand[j]])

        backstack(board, hand, [])
        return min(res) if res else -1

    @staticmethod
    def resolve_str(_board_loop):
        n = 1
        while n:
            _board_loop, n = re.subn(r'(.)\1{2,}', '', _board_loop)
        return _board_loop


if __name__ == '__main__':
    print(Solution().findMinStep("GGRRGRRYY", "RYRBR"), 3)
    print(Solution().findMinStep("RRYGGYYRRYYGGYRR", "GGBBB"), 5)
    print(Solution().findMinStep("BRWGWYY", "YGBWY"), "-1")
    print(Solution().findMinStep("RRWWRRBBRR", "WB"), "2")
    print(Solution().findMinStep("RRWWRRW", "WR"), '-1')
    print(Solution().findMinStep("WRRBBW", "RB"), '-1')
    print(Solution().findMinStep("WWRRBBWW", "WRBRW"), '2')
    print(Solution().findMinStep("G", "GGGGG"), '2')
    print(Solution().findMinStep("RBYYBBRRB", "YRBGB"), '3')
