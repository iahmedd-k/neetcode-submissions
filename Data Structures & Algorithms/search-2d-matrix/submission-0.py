class Solution:

    def searchMatrix(self, grid, target):

        row_count = len(grid)
        col_count = len(grid[0])

        left = 0
        right = row_count * col_count - 1

        while left <= right:

            mid = (left + right) // 2

            # convert 1D index → 2D position
            row = mid // col_count
            col = mid % col_count

            value = grid[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False