class Search2DMatrix2:
    def brute(self,matrix,target):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return[i,j]
        return[-1,-1]
    
    def better(self, matrix,target):
        def binarySearch(matrix,target):
            n = len(matrix)

            low = 0
            high = n-1
            while low<= high:
                mid = (low + high)//2
                if matrix [mid] == target:
                    return mid
                elif matrix[mid]<target:
                    low= mid + 1
                else:
                    high = mid -1
            return -1
        
        for r,row  in enumerate(matrix):
            indx = binarySearch(row,target)
            if indx != -1:
                return [r,indx]
        return [-1,-1]
    
    def optimal(self, matrix,target):
        row = 0
        col = len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return [row,col]
            elif matrix[row][col] > target:
                col -=1
            else:
                row +=1
        return [-1,-1]

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
solution = Search2DMatrix2()
print(solution.brute(matrix,target))
print(solution.better(matrix,target))
print(solution.optimal(matrix,target))