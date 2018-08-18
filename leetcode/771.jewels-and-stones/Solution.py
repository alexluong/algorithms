class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        for c in S:
            if c in J:
                num += 1

        return num

J = "z"
S = "ZZ"
print(Solution().numJewelsInStones(J, S))