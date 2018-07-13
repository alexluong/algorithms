class Solution:
    def compareString(self, str1, str2):
        v1Int = int(str1) if str1 != "" else 0
        v2Int = int(str2) if str2 != "" else 0
        if v1Int > v2Int:
            return 1
        elif v1Int < v2Int:
            return -1
        else:
            return 0

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = ""
        v2 = ""
        r1 = 0
        r2 = 0
        stop1 = False
        stop2 = False
        while 1:
            if r1 < len(version1) and version1[r1] != ".":
                v1 += version1[r1]
            else:
                stop1 = True

            if r2 < len(version2) and version2[r2] != ".":
                v2 += version2[r2]
            else:
                stop2 = True

            if stop1 and stop2:
                compare = self.compareString(v1, v2)
                if compare != 0 or (r1 >= len(version1) and r2 >= len(version2)):
                    return compare
                v1 = ""
                v2 = ""
                stop1 = False
                stop2 = False

            if not stop1: r1 += 1
            if not stop2: r2 += 1

        if len(version1) != len(version2):
            return self.compareString(v1, v2)

        return 0

print(Solution().compareVersion("1", "1.0"))