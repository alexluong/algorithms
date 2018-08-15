class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        S = str(num)
        if (len(S) > 1):
            max = S[0]
            maxIndex = 0
            for i in range(1, len(S)):
                if S[i] >= max:
                    max = S[i]
                    maxIndex = i

            if S[0] != max:
                first = S[0]
                S = max + S[1:]
                S = S[:maxIndex] + first + S[maxIndex + 1:]
            elif int(S[1:]) != 0:
                S = S[0] + str(self.maximumSwap(S[1:]))
        
        return int(S)

print(Solution().maximumSwap(11000))