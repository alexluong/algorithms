class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        l = len(word)
        if l == 1:
            return True

        first = word[0]
        if first.islower():
            correct = all(c.islower() for c in word[1:])
        else:
            second = word[1]
            if second.islower():
                correct = all(c.islower() for c in word[2:])
            else:
                correct = all(c.isupper() for c in word[2:])

        return correct


word = "FL"

print(Solution().detectCapitalUse(word))