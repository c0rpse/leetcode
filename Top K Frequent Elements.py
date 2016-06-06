from sys import maxint
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return nums
        if k < 1:
            return []
        if k > len(nums):
            return list(set(nums))
        hash_list = dict()
        for i in nums:
            if i in hash_list.keys():
                hash_list[i] += 1
            else:
                hash_list.setdefault(i,1)

        sorted_hash_list = sorted(hash_list.iteritems(), key=lambda d: d[1], reverse=True)
        ret = list()
        for i in xrange(k):
            ret.append(sorted_hash_list[i][0])
        return ret

if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,4,5,2,3,1,4,3,2,6,7,8,9,9,0]
    print s.topKFrequent(l,9)

