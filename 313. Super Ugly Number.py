class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        primes_list = [1] * len(primes)
        primes_seq_list = [-1] * len(primes)
        tmp_list = [0] * len(primes)
        ugly_list, index = [1], 0
        while index < n-1:
            for i in xrange(len(primes)):
                tmp_list[i] = primes[i] * primes_list[i]
            ugly_min = min(tmp_list)
            print tmp_list,ugly_min
            for i in xrange(len(tmp_list)):
                if tmp_list[i] == ugly_min:
                    primes_seq_list[i] += 1
                    primes_list[i] = primes[primes_seq_list[i]]
                    break
            index += 1
            if ugly_list[-1] < ugly_min:
                ugly_list.append(ugly_min)
            else:
                index -= 1
        return ugly_list[n-1]
s = Solution()
print s.nthSuperUglyNumber(14,[2,7,13,19])

