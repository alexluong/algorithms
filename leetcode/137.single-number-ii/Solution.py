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
                obj[s] += 1
                if obj[s] == 3:
                    obj.pop(s)
            else:
                obj[s] = 1

        return int(list(obj)[0])

nums = [0,1,0,1,0,1,99]

print(Solution().singleNumber(nums))