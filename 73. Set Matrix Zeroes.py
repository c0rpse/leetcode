class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_list, column_list = [], []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_list.append(i)
                    column_list.append(j)
        row_list, column_list = list(set(row_list)), list(set(column_list))
        for row in row_list:
            for col in xrange(len(matrix[row])):
                matrix[row][col] = 0
        for column in column_list:
            for row in xrange(len(matrix)):
                matrix[row][column] = 0




