class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:

            # S1 Remove the first row
            ret += matrix.pop(0)

            # S2 add the last element of the list from matrix
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # S3 last row in rev order
            if matrix:
                ret += matrix.pop()[::-1]

            # S4 add the 1st element of the list from matrix
            if matrix and matrix[0]:
                for col in matrix[::-1]:
                    ret.append(col.pop(0))

        return ret