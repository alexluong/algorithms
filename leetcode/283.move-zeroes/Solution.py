class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return

        length = len(nums)
        firstIndex = nums.index(0)
        i = firstIndex
        while i < length:
            if i != 0:
                self.swap(nums, firstIndex, i)
                firstIndex = nums.index(0)
            i += 1


nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
Solution().moveZeroes(nums)
print(nums)
