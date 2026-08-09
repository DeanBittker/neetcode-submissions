class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, len_rows = len(matrix), len(matrix[0])
        L = 0
        R = (num_rows * len_rows) -1
        while L <= R:
            mid = (L+R)//2
            row = mid // len_rows
            idx = mid % len_rows
            if target > matrix[row][idx]:
                L = mid + 1
            elif target < matrix[row][idx]:
                R = mid - 1
            else:
                return True
        return False
