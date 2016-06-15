class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cur_row = len(matrix) - 1
        while cur_row >= 0:
            if target == matrix[cur_row][0]:
                return True
            elif target > matrix[cur_row][0]:
                return self.binarySearch(matrix[cur_row], target)
            else:
                cur_row -= 1
        return False

    def binarySearch(self, row_list, target):
        begin, end = 0, len(row_list) - 1
        while begin <= end:
            middle = begin + (end - begin) // 2
            if row_list[middle] == target:
                return True
            elif row_list[middle] < target:
                begin = middle + 1
            else:
                end = middle - 1
        return False


