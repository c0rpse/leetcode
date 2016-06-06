class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bit_list = list()
        for word in words:
            word_bit_map = 0
            for char in word:
                word_bit_map |= 1 << (ord(char) - ord('a'))
            bit_list.append(word_bit_map)

        max_product = 0
        for i in xrange(len(words)):
            j = i+1
            while j < len(words):
                if bit_list[i] & bit_list[j] == 0 and len(words[i])*len(words[j]) > max_product:
                    max_product = len(words[i])*len(words[j])
                j += 1
        return max_product



s = Solution()
l = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
x = s.maxProduct(l)
print x