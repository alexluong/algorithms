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
                obj[s] = True

        return int(list(obj)[0])

nums = [4,1,2,1,2]

print(Solution().singleNumber(nums))