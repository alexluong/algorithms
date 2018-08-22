class Solution:
    def canPlaceFlower(self, flowerbed, i):
        canPlace = False

        if flowerbed[i] == 0:
            if i == 0:
                if len(flowerbed) == 1 or flowerbed[i + 1] == 0:
                    canPlace = True
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0:
                    canPlace = True
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                canPlace = True

        return canPlace

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        i = 0
        while i < len(flowerbed) and n > 0:
            if self.canPlaceFlower(flowerbed, i):
                n -= 1
                flowerbed[i] = 1

            i += 1

        return n == 0

flowerbed = [0]
n = 1

print(Solution().canPlaceFlowers(flowerbed, n))