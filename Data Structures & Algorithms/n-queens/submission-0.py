class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        colSet, negDiag, posDiag = set(), set(), set()
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in colSet or (r-c) in negDiag or (r + c) in posDiag:
                    continue

                colSet.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                board[r][c] = "Q"

                dfs(r + 1)

                colSet.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = "."

        dfs(0)
        return res