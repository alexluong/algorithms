class Solution: 
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        R1 = {}
        for i in range(0, len(list1)):
            r = list1[i]
            R1[r] = i

        common = {}
        for i in range(0, len(list2)):
            r = list2[i]
            if r in R1:
                index = str(R1[r] + i)
                if index in common:
                    common[index].append(r)
                else:
                    common[index] = [r]

        keys = common.keys()
        intKeys = [int(key) for key in keys]

        return common[str(min(intKeys))]


list1 = ["cbe","dcb","bbd","ddb","KFC"]
list2 = ["cbc","bad","bcb","bbd","eda","edc","ddb","KFC"]

print(Solution().findRestaurant(list1, list2))