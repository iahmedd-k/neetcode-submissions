class Solution:
    def isValidSudoku(self, board):
        import collections

        rows = collections.defaultdict(set)    # rows[i] = set of numbers in row i
        cols = collections.defaultdict(set)    # cols[j] = set of numbers in col j
        boxes = collections.defaultdict(set)   # boxes[(i//3, j//3)] = 3x3 box

        for i in range(9):                     # loop through rows
            for j in range(9):                 # loop through columns
                val = board[i][j]

                if val == ".":                 # skip empty cells
                    continue

                box_key = (i // 3, j // 3)

                if (val in rows[i] or
                    val in cols[j] or
                    val in boxes[box_key]):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_key].add(val)

        return True