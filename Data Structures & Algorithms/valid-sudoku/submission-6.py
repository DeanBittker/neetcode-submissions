class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        squares = [[set() for i in range(3)] for j in range (3)]

        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_set = squares[r//3][c//3]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in box_set:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                box_set.add(val)
        return True


            