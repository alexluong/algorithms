class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        LOWER_UPPER_DIFF = 32
        newStr = ""
        for c in str:
            asciiValue = ord(c)
            if asciiValue >= 65 and asciiValue <= 90: # is Uppercase
                c = chr(asciiValue + LOWER_UPPER_DIFF)
            newStr += c

        return newStr

print(Solution().toLowerCase("Hello"))