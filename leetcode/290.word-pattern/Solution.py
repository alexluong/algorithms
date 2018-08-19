class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()

        if len(pattern) != len(words):
            return False

        patObj = {}
        wordObj = {}
        isMatch = True

        for i in range(0, len(pattern)):
            c = pattern[i]
            word = words[i]
            if c in patObj:
                if patObj[c] != word:
                    isMatch = False
                    break
                if wordObj[word] != c:
                    isMatch = False
                    break
            else:
                if (word in wordObj):
                    isMatch = False
                    break
                patObj[c] = word
                wordObj[word] = c

        return isMatch

pattern = "ab"
str = "dog dog"

print(Solution().wordPattern(pattern, str))