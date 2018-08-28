class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 5
        while n / i >= 1:
            count += int(n / i)
            i *= 5
        return count

print(Solution().trailingZeroes(3))