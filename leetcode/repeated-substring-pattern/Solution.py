class Solution:
    def checkIfThisIsPattern(self, s, index):
        length = len(s)
        if length % (index + 1) != 0:
            return False

        return s == s[0: index + 1] * int((length / (index + 1)))

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        lastChar = s[length - 1]
        start = 0
        index = s.find(lastChar, start)
        while (index != length - 1):
            if (self.checkIfThisIsPattern(s, index)):
                return True
            start = index + 1
            index = s.find(lastChar, start)

        return False

print(Solution().repeatedSubstringPattern("a"))