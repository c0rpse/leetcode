import sys
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not len(matrix):
            return False
        row, rows = 0, len(matrix)
        columns, column = len(matrix[0]), len(matrix[0]) - 1
        while row < rows and column >= 0:
            if column < 0:
                column = len(matrix[row]) - 1
            if matrix[row][column] > target:
                column -= 1
                continue
            elif matrix[row][column] < target:
                row += 1
                continue
            else:
                return True
        return False


s = Solution()
print s.searchMatrix([[-1,3]],-1)

