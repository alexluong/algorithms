class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strLength = len(strs)
        if strLength == 0:
            return ""
        firstStr = strs[0]
        if strLength == 1:
            return firstStr

        end = False
        commonNum = 0
        while not end:
            if commonNum == len(firstStr):
                end = True
                break

            for i in range(1, strLength):
                if commonNum == len(strs[i]) or strs[i][commonNum] != firstStr[commonNum]:
                    end = True
                    break
            
            if not end:
                commonNum += 1

        return firstStr[0: commonNum]

print(Solution().longestCommonPrefix(["", "", ""]))