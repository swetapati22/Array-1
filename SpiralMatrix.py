# Time Complexity :
- O(m * n), where m is the number of rows and n is the number of columns

# Space Complexity :
- O(1), excluding the output array which is required to return the result

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse downwards
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse from right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse upwards
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result

