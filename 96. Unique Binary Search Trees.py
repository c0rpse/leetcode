class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list()
        for i in range(0, n+1):
            nums.append(0)
            if i < 2:
                nums[i] = 1
            else:
                for j in range(1, i+1):
                    nums[i] += nums[j-1]*nums[i-j]
        return nums[n]

if __name__ =='__main__':
    s = Solution()
    print  s.numTrees(3)






