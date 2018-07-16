class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        while num != 1:
            if num % 4 != 0:
                return False
            num = num // 4
             
        return True
        
print(Solution().isPowerOfFour(4))