class Search2DMatrix:
    def brute( self,matrix,target):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False
    
    def better( self,matrix, target):
        def binary_search(matrix,target):
            n = len(matrix)
            low = 0
            high = n-1

            while low <= high:
                mid = (low+ high)//2
                if matrix[mid] == target:
                    return True
                elif target > matrix[mid]:
                    low = mid + 1
                else:
                    high = mid -1
            return False

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                return binary_search(matrix[i],target)
        return False
    def optimal(self,matrix,target):
        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n*m -1

        while low <= high:
            mid = (low + high)//2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid -1

        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution = Search2DMatrix()
print(solution.brute(matrix,target))
print(solution.better(matrix,target))
print(solution.optimal(matrix,target))