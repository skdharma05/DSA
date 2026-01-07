class MedainOf2DMatrix:
    def brute(self,matrix):
        n = len(matrix)
        m = len(matrix[0])
        dummpy= []
        for i in range(n):
            for j in range(m):
                dummpy.append(matrix[i][j])
        dummpy.sort()
        return dummpy[(n*m)//2]

    def optimal(self,matrix):
        def upperBound(nums,k):
            n = len(nums)
            low =0
            high = n -1
            ans = n

            while low<=high:
                mid = (low+high)//2
                if nums[mid]>k:
                    ans = mid
                    high = mid -1
                else:
                    low = mid +1
            return ans

        n = len(matrix)
        m = len(matrix[0])
        required = (n*m)//2


        low = min(row[0] for row in matrix)
        high = max(row[-1] for row in matrix)

        while low <= high:
            mid = (low + high)//2
            count = 0
            for row in matrix:
                count+= upperBound(row,mid)

            if count <= required:
                low = mid + 1
            else:
                high = mid - 1

        return low            
        

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]

solution = MedainOf2DMatrix()
print(solution.brute(matrix))
print(solution.optimal(matrix))