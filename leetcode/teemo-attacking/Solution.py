class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        length = len(timeSeries)
        if length == 0:
            return 0
        if length == 1:
            return duration

        total = 0
        before = timeSeries[0]
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - before >= duration:
                total += duration
            else:
                total += timeSeries[i] - before
            before = timeSeries[i]

        total += duration
        return total
                

print(Solution().findPoisonedDuration([], 2))