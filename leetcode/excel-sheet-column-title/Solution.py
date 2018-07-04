import math

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ALL_C = 26
        START = 64 # a == 65

        val = ""
        num = n
        while num > ALL_C:
            remnant = num % ALL_C
            if remnant == 0:
                remnant = ALL_C

            val = chr(START + remnant) + val
            num = math.ceil(num / ALL_C) - 1

        if num > 0:
            val = chr(START + num) + val
        return val

print(Solution().convertToTitle(701))