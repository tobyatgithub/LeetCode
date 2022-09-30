"""
Sep 29 2022:
The most challenging part here is to mark the 'seen' elements.
I initially tried to do it was a set, but that passing the set
around is messy and TLE on LC.
Another way here is to modify the graph/board on the fly, and 
here is an important backtracking technique!
1. you first check boundary condition (row, col, etc.)
2. check True condition (element == )
3. visit the current node (modify)
4. use a for-loop to dfs
5. outside of the for-loop, convert the modified back 
(so it doesn't affect other nodes' searchs)

This convert back mechanism is interesting and totally new to me!
"""
import numpy as np


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if (
            row < 0
            or row == self.ROWS
            or col < 0
            or col == self.COLS
            or self.board[row][col] != suffix[0]
        ):
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = "#"
        print(np.matrix(self.board))
        print()
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret:
                break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret


a = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "E", "E", "E"]]
word = "FEEEC"
res = Solution().exist(board=a, word=word)
print(res)
