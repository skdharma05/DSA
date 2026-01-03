class FindRowsWithMaxNumOnce:
    def brute(self, mat):
        n =len(mat)
        m =len(mat[0])

        indx = -1
        max_cout = 0
        for i in range(n):
            count =0
            for j in range(m):
                count+=mat[i][j]
            if count>max_cout:
                max_cout = count
                indx =i
        return indx
    
    def optimal(self, mat):
        def low(mat,k):
            n = len(mat)
            low =0
            high = n-1
            ans = n
            while low <= high:
                mid = (low + high)//2
                if mat[mid]>=k:
                    ans = mid 
                    high = mid -1
                else:
                    low = mid + 1
            return ans
        
        n= len(mat)
        m = len(mat[0])
        row_indx = -1
        max_count =0
        for i in range (n):
            once_count = low(mat[i],1)
            count = m - once_count
            if count > max_count:
                max_count = count
                row_indx =i
        
        return row_indx


mat1 = [ [0, 0], [0, 0] ]
mat2 = [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ]
solution = FindRowsWithMaxNumOnce()
print(solution.brute(mat1))
print(solution.brute(mat2))
print(solution.optimal(mat1))
print(solution.optimal(mat2))