class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        seen = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i >= len(word):
                self.res = True
                return

            if r >= ROWS or c >= COLS or r < 0 or c < 0 or board[r][c] != word[i] or (r, c) in seen:
                return False

            seen.add((r, c))
            print(seen)
            dfs(r+1, c, i+1)
            dfs(r-1, c, i+1)
            dfs(r, c+1, i+1)
            dfs(r, c-1, i+1)
            
            seen.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, 0)
                
        return self.res
            