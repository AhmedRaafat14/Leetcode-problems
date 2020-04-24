class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        islands = 0
        rows, cols = len(grid), len(grid[0])
        # stack = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    # stack.append((row, col))
                    # for rw, co in stack:
                    #     if 0 <= rw < rows and 0 <= co < cols and grid[rw][co] == '1':
                    #         grid[rw][co] = '0'
                    #         stack.extend([(rw + 1, co), (rw - 1, co), (rw, co + 1), (rw, co - 1)])
                    self.rest_of_island(row, col, grid)
        return islands

    def rest_of_island(self, row, col, grid):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != '1':
            return
        grid[row][col] = '0'
        self.rest_of_island(row, col + 1, grid)
        self.rest_of_island(row, col - 1, grid)
        self.rest_of_island(row + 1, col, grid)
        self.rest_of_island(row - 1, col, grid)
