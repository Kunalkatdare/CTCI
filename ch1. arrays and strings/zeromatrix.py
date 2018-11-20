class Solution:
    def ZeroMatrix(self, mat):
        if len(mat) == 0:
            return mat
        m = len(mat[0])
        n = len(mat)
        zero_row, zero_col = [], []
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    zero_row.append(r)
                    zero_col.append(c)
        for r in zero_row:
            for c in range(m):
                mat[r][c] = 0
        for c in zero_col:
            for r in range(n):
                mat[r][c] = 0
        return mat


def main():
    mat = [[1, 2, 3],
           [2, 0, 6],
           [1, 4, 2]]
    result = Solution().ZeroMatrix(mat)
    print(result)


if __name__ == '__main__':
    main()
