class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i

            if target < nums[i]:
                return i
            
        return len(nums)

print(Solution().searchInsert([1,3,5,6], 2))