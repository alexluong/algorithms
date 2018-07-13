class Solution(object):
    def isPalindrome(self, s):
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                print(s[low:high + 1])
                if self.isPalindrome(s[low + 1: high + 1]):
                    return True
                elif self.isPalindrome(s[low: high]):
                    return True
                else:
                    return False
                
        return True

        
print(Solution().validPalindrome("abc"))