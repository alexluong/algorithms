class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
            ["z", "x", "c", "v", "b", "n", "m"]
        ]

        returnList = []
        for word in words:
            firstLetter = word[0].lower()
            if firstLetter in keyboard[0]: row = 0
            elif firstLetter in keyboard[1]: row = 1
            else: row = 2

            sameRow = True
            for letter in word:
                if letter.lower() not in keyboard[row]:
                    sameRow = False

            if sameRow: returnList.append(word)

        return returnList

print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))