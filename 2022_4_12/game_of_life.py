# https://leetcode.com/problems/game-of-life/
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for row, x in enumerate(board):
            for col in range(len(x)):

                increment = 1 if board[row][col] > 0 else -1
                # board[row][col] = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if -1 < row + i < len(board) and -1 < col + j < len(x) and not (i == 0 and j == 0):
                            board[row][col] += increment if board[row + i][col + j] > 0 else 0
        for row, x in enumerate(board):
            for col in range(len(x)):
                val = board[row][col]
                if val > 0:
                    board[row][col] = 1 if val in [3, 4] else 0
                else:
                    board[row][col] = 1 if val == -3 else 0


board = [[1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0]]
Solution().gameOfLife(board)
print(board)
