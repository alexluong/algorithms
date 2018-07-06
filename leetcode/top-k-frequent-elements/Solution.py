class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        obj = {}
        for num in nums:
            stringNum = str(num)
            if stringNum not in obj:
                obj[stringNum] = 1
            else:
                obj[stringNum] += 1

        items = list(obj.items())
        # sortList = sorted(items, key=lambda: (k, v): (v, k))
        sortList = sorted(items, key=lambda item: item[1], reverse=True)
        returnList = []
        for i in range(0, k):
            returnList.append(int(sortList[i][0]))

        return returnList

print(Solution().topKFrequent([1,1,1,2,2,3], 2))