firstBadVersion = 1

def isBadVersion(n):
    if n >= firstBadVersion:
        return True
    return False

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def checkBadVersion(self, start, end):
        if end == start + 1:
            if isBadVersion(start):
                if start != 0 and isBadVersion(start - 1):
                    return start - 1
                return start
            return end
                

        mid = (start + end) // 2

        if isBadVersion(mid):
            if mid == 0 or not isBadVersion(mid - 1):
                return mid
            return self.checkBadVersion(start, mid)
        else:
            return self.checkBadVersion(mid, end)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.checkBadVersion(0, n)

print(Solution().firstBadVersion(1))