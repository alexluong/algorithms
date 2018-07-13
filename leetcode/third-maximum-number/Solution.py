class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = None
        second = None
        third = None
        for num in nums:
            if first == None: first = num
            elif second == None:
                if num > first:
                    second = first
                    first = num
                elif num == first: continue
                else: second = num
            else:
                if num == first or num == second or num == third:
                    continue
                    
                if num > first:
                    third = second
                    second = first
                    first = num
                elif num > second:
                    third = second
                    second = num
                elif third == None or num > third:
                    third = num

        print({
            "first": first,
            "second": second,
            "third": third
        })
        if third == None:
            third = first
        return third

print(Solution().thirdMax([2, 2, 0, 1]))