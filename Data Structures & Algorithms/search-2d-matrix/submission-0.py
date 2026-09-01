class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        row = -1
        while top <= bottom:
            mid = (top + bottom)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1

        if row == -1:
            return False
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target == matrix[row][mid]:
                return True
            if target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False