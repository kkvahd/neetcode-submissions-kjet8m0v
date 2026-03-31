class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        cols = len(matrix[0]) - 1

        while t <= b:
            m = (t + b) // 2

            if matrix[m][0] > target:
                b = m - 1
            elif matrix[m][cols] < target:
                t = m + 1
            else:
                l, r = 0, cols

                while l <= r:
                    n = (l + r) // 2
                    
                    if matrix[m][n] > target:
                        r = n - 1
                    elif matrix[m][n] < target:
                        l = n + 1
                    else:
                        return True
                return False
        return False