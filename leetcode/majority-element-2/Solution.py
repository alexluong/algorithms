class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        threshold = length / 3
        arr = []

        obj = {}
        for num in nums:
            stringNum = str(num)
            if stringNum not in obj:
                obj[stringNum] = 1
            else:
                obj[stringNum] += 1
            
            if obj[stringNum] > threshold:
                if num not in arr:
                    arr.append(num)
        
        return arr

print(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))