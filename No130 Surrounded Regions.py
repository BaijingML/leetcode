class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    self.infect(board, i, j, m, n)
                else:
                    continue
        print(board)

    def infect(self, board, i, j, m, n):
        if 1 <= i < m - 1 and 1 <= j < n - 1 and board[i][j] == 'O':
            print(i, j)
            board[i][j] = 'X'
            self.infect(board, i + 1, j, m, n)
            self.infect(board, i - 1, j, m, n)
            self.infect(board, i, j + 1, m, n)
            self.infect(board, i, j - 1, m, n)


if __name__ == '__main__':
    Solu = Solution()
    print(Solu.solve([["O","O","O"],["O","O","O"],["O","O","O"]]))
