class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        threshold = length / 2

        obj = {}
        for num in nums:
            stringNum = str(num)
            if stringNum not in obj:
                obj[stringNum] = 1
            else:
                obj[stringNum] += 1
            
            if obj[stringNum] > threshold:
                returnVal = num
                break
        
        return returnVal

print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))