class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        col = len(matrix)
        row = len(matrix[0])

        for i in range(0, row):
            num = matrix[0][i]
            curRow = i + 1
            for j in range(1, col):
                if curRow >= row:
                    break

                if matrix[j][curRow] == num:
                    curRow += 1
                else:
                    return False

        for i in range(0, col):
            num = matrix[i][0]
            curCol = i + 1
            for j in range(1, row):
                if curCol >= col:
                    break

                if matrix[curCol][j] == num:
                    curCol += 1
                else:
                    return False

        return True

matrix = [
    [18],[66]
]


print(Solution().isToeplitzMatrix(matrix))