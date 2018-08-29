from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        C = Counter()
        for i in range(0, len(s)):
            c = s[i]
            if c not in C:
                C[c] = {
                    "index": i,
                    "appearances": 1
                }
            else:
                C[c]["appearances"] += 1

        minIndex = None
        for c in C:
            obj = C[c]
            if obj["appearances"] == 1:
                if minIndex == None:
                    minIndex = obj["index"]
                elif obj["index"] < minIndex:
                    minIndex = obj["index"]

        return minIndex if minIndex != None else -1

s = "loveleetcode"

print(Solution().firstUniqChar(s))