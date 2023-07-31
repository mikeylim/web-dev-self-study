class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        lastIndex = len(matrix) - 1
        for i in range(lastIndex):
            for j in range(lastIndex):
                matrix[i][j] = matrix[lastIndex][j]

        return matrix

sol = Solution()
print(sol.rotate([[1,2,3], [4,5,6], [7,8,9]]))

    # [1,2,3]
    # [4,5,6]
    # [7,8,9]

    # [7,4,1]
    # [8,5,2]
    # [9,6,3]