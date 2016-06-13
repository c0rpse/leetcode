class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in xrange(len(matrix)):
            self.circle_conv(matrix, i)

    def circle_conv(self, matrix, circle):
        matrix_len = len(matrix)
        matrix_mid = matrix_len//2 + 1 if matrix_len & 0x1 else matrix_len//2
        if circle > matrix_mid:
            return
        matrix_len -= 1
        left, right = circle, matrix_len - circle
        for idx in xrange(left, right):
            self.conv(matrix, circle, idx)

    def conv(self, matrix, m, n):
        c = len(matrix) - 1
        top, right, bottom, left = (m, n), (n, c - m), (c - m, c - n), (c - n, m)
        self.swap(matrix, left, bottom)
        self.swap(matrix, bottom, right)
        self.swap(matrix, right, top)

    def swap(self, matrix, i, j):
        tmp = matrix[i[0]][i[1]]
        matrix[i[0]][i[1]] = matrix[j[0]][j[1]]
        matrix[j[0]][j[1]] = tmp

s = Solution()
l = [[1, 2, 3,4], [ 5, 6, 7, 8], [9,10,11,12],[13,14,15,16]]
s.rotate(l)
print l


