# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        rows, cols = binaryMatrix.dimensions()

        if rows == 0 or cols == 0:
            return -1
        ans = -1
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                ans = col
                col -= 1
            else:
                row += 1
        return ans
