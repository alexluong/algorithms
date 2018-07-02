class Solution(object):
    def binarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            midValue = nums[mid]
            if midValue == target:
                return mid
            elif midValue > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = self.binarySearch(nums, target)

        if index == -1:
            return [-1, -1]

        firstIndex = index
        lastIndex = index
        while firstIndex != 0 and nums[firstIndex - 1] == target:
            firstIndex -= 1
        while lastIndex != len(nums) - 1 and nums[lastIndex + 1] == target:
            lastIndex += 1

        return [firstIndex, lastIndex]

print(Solution().searchRange([0, 1], 1))
# print(Solution().binarySearch([5, 7, 7, 8, 8, 10], 8))