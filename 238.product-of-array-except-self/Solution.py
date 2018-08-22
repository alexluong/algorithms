class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)

        left = [1] * l
        for i in range(1, l):
            left[i] = left[i - 1] * nums[i - 1]

        right = [1] * l
        for i in reversed(range(0, l - 1)):
            right[i] = right[i + 1] * nums[i + 1]

        return [i * j for i, j in zip(left, right)]


nums = [1,2,3,4]

print(Solution().productExceptSelf(nums))