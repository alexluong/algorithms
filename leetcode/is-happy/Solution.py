import math

class Solution:
    def getDigits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 10:
            return [n]

        return [n % 10] + self.getDigits(math.floor(n / 10))
        

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happy = True
        numList = [n]
        num = n
        while num != 1:
            digits = self.getDigits(num)
            num = 0
            for digit in digits:
                num += digit * digit
            
            if num in numList:
                happy = False
                break
            
            numList.append(num)

        return happy

print(Solution().isHappy(145))