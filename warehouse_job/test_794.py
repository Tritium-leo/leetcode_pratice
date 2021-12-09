from typing import *


# difficulty = middle


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        ans = False
        # 无 连续
        full_str = ''.join(board)
        full_flag = ' ' in full_str
        if full_str.strip() == "":
            return True
        o_count = full_str.count('O')
        x_count = full_str.count('X')
        o_x_diff = x_count - o_count
        # X -O  的差距需要在 0,1之间
        if o_x_diff not in (0, 1):
            return ans
        # 转置
        T = [board[0][idx] + board[1][idx] + board[2][idx] for idx in range(len(board))]
        T_set = [len(set(x)) == 1 and x[0] != ' ' for x in T]
        if T_set.count(True) > 1:
            return ans
        board_set = [len(set(x)) == 1 and x[0] != ' ' for x in board]
        if board_set.count(True) > 1:
            return ans
        x_set = [len(set(board[0][0] + board[1][1] + board[2][2])) == 1 and board[1][1] != ' ',
                 len(set(board[0][2] + board[1][1] + board[2][0])) == 1 and board[1][1] != ' ']
        # 横竖 仅有一个 斜 可能有两个 数量关系不一定正确
        over_check = T_set + board_set + x_set
        code_set = {T[idx][0] for idx, x in enumerate(T_set) if x}.union(
            {board[idx][0] for idx, x in enumerate(board_set) if x}).union({board[1][1] for _ in x_set if _})
        if len(code_set) > 1:
            return ans
        # 存在三个连续数字

        if any(over_check):
            check_code = code_set.pop()
            if check_code == "X" and (o_count + x_count) % 2 == 1:
                ans = True
            elif check_code == "O" and (o_count + x_count) % 2 == 0:
                ans = True
        elif len(set(over_check)) == 1 and over_check[0] == False:
            ans = True
        return ans


if __name__ == "__main__":
    input_check = [
        (["XXX", " X ", "OOO"], False),
        (["XOX", " X ", "   "], False),
        (["XXX", "   ", "OOO"], False),
        (["XOX", "O O", "XOX"], True),
        (["O  ", "   ", "   "], False),
        (["XO ", "XO ", "XO "], False),
        (["   ", "   ", "   "], True),
        (["XXX", "XOO", "OO "], False),
        (["XXX", "OOX", "OOX"], True),
        (["X  ", "X  ", "O O"], True),
        (["X  ", "   ", "   "], True)
    ]
    for _in, _ans in input_check:
        ans = Solution().validTicTacToe(_in)
        if ans != _ans:
            print(f'ERRor:Need:{_ans},but YOUR IS:{ans}')

    print('done')
