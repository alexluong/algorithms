class Solution:
    def fib(self, n):
        if n == 1 or n == 2:
            return n

        minusTwo = 1
        minusOne = 2
        for i in range(2, n):
            value = minusTwo + minusOne
            minusTwo = minusOne
            minusOne = value
        
        return minusOne

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fib(n)
        

print(Solution().climbStairs(35))