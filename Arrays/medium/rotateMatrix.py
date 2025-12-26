#Rotate matrix by 90 degrees clockwise
def brute(matrix):
    n = len(matrix)

    ans = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ans[j][n-i-1]=matrix[i][j]
    
    return ans

def optimal(matrix):
    n = len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()

    return matrix


def main():
    matrix = [[1,2,3,4],[5,6,7,8],[ 9,10,11,12],[13,14,15,16]]
    result = optimal(matrix)
    print(result)
main()