class PeakElement2D:
    def optimal (self,mat):
        def helper(mat,col):
            n= len(mat)
            index = -1
            max_value = float('-inf')
            for i in range(n):
                if mat[i][col]>max_value:
                    max_value = mat[i][col]
                    index = i
            return index
        
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        while low <= high:
            mid = (low + high)//2
            row = helper(mat,mid)
            left = mat[row][mid-1] if mid - 1 >= 0 else float('-inf')
            right = mat[row][mid+1] if mid + 1 < m else float('-inf')

            if mat[row][mid] >left and mat[row][mid]>right:
                return [ row, mid]
            elif mat[row][mid] <left :
                high = mid -1
            else:
                low = mid + 1

        return [-1,-1]

mat = [
    [4, 2, 5, 1, 4, 5],
    [2, 9, 3, 2, 3, 2],
    [1, 7, 6, 0, 1, 3],
    [3, 6, 2, 3, 7, 2]
]
solution = PeakElement2D()
print(solution.optimal(mat))