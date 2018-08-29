from collections import Counter

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        A = Counter()
        C = {}
        maxApp = 0
        for c in s:
            if c in A:
                appearance = A[c] + 1
                if appearance > maxApp:
                    maxApp = appearance

                # Pop from old dict
                C[str(A[c])].pop(c)

                # Append in new dict
                if str(appearance) in C:
                    C[str(appearance)][c] = True
                else:
                    C[str(appearance)] = { c: True }
            else:
                if maxApp == 0:
                    maxApp = 1

                if "1" in C:
                    C["1"][c] = True
                else:
                    C["1"] = { c: True }
            
            A[c] += 1

        res = ""
        for i in reversed(range(1, maxApp + 1)):
            for c in C[str(i)].keys():
                res += c * i

        return res

s = ""

print(Solution().frequencySort(s))