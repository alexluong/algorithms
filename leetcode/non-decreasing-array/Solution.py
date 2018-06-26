class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isPossible = True
        before = None
        running = nums[0]
        larger = 0
        for i in range(len(nums)):
            num = nums[i]

            if num < running:
                larger = larger + 1
                if larger == 2:
                    isPossible = False
                    break
                if i > 1 and before > num:
                    if i != len(nums) - 1 and running > nums[i + 1]:
                        isPossible = False
                        break

            if i != 0:
                before = running
            running = num
        
        return isPossible

print(Solution().checkPossibility([1, 2, 4, 5, 3]))