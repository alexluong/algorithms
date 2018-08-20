class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        obj = {}

        for num in nums:
            s = str(num)
            if s in obj:
                obj.pop(s)
            else:
                obj[s] = 1

        return [int(key) for key in list(obj)]

nums = [1,2,1,3,2,5]

print(Solution().singleNumber(nums))