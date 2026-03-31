class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        grid_dict = {}

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".":
                    continue
                if r not in row_dict:
                    row_dict[r] = {curr}
                elif curr not in row_dict[r]:
                    row_dict[r].add(curr)
                else:
                    return False

                if c not in col_dict:
                    col_dict[c] = {curr}
                elif curr not in col_dict[c]:
                    col_dict[c].add(curr)
                else:
                    return False

                grid = tuple([r // 3, c // 3])
                if grid not in grid_dict:
                    grid_dict[grid] = {curr}
                elif curr not in grid_dict[grid]:
                    grid_dict[grid].add(curr)
                else:
                    return False
        return True