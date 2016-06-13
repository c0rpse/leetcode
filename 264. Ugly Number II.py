# encoding:utf-8
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_list = [1]
        k2, k3, k5 = 0, 0, 0
        i = 0
        while i < n:
            k2_val, k3_val, k5_val = [ugly_list[k2] * 2, ugly_list[k3] * 3, ugly_list[k5] * 5]
            min_ugly = min([k2_val, k3_val, k5_val])
            if min_ugly == k2_val:
                k2 += 1
            elif min_ugly == k3_val:
                k3 += 1
            elif min_ugly == k5_val:
                k5 += 1
            i += 1
            #如果min_ugly小于等于当前最大元素,说明其已经在list中
            if min_ugly > ugly_list[-1]:
                ugly_list.append(min_ugly)
            else:
                i -= 1
        return ugly_list[n-1]

s = Solution()
print s.nthUglyNumber(7)