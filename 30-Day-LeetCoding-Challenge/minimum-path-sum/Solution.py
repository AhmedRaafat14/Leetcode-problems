class Solution:
    def minPathSum(self, grid):
        '''
        the first row each column equal the sum of itself with the previous colmuns.
        The same applied for the first column, the first column of each row equals the sume of itself with the previous ones in.
        '''
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    grid[0][col] += grid[0][col - 1]
                elif col == 0:
                    grid[row][0] += grid[row - 1][0]
                else:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

        return grid[-1][-1]
