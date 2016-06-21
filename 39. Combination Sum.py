class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        comb = list()
        if not candidates or not target or len(candidates) < 1:
            return comb
        cur = list()
        self.backtrack(0, candidates, comb, cur, 0, target)
        return comb

    def backtrack(self, start, candidates, all_data, cur, summary, target):
        if summary == target:
            tmp = cur[:]
            tmp.sort()
            all_data.append(tmp)
            return
        if summary > target:
            return
        for i in xrange(start, len(candidates)):
            if (summary + candidates[i]) <= target:
                cur.append(candidates[i])
                self.backtrack(i, candidates, all_data, cur, summary + candidates[i], target)
                cur.pop()

s = Solution()
print s.combinationSum([2, 3, 6, 7], 7)
