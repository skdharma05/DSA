def leftRotateArrayByOnePlace(arr):
    n = len(arr)
    first = arr[0]

    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = first 

    return arr  

def rightRotateArrayByOnePlace(arr):
    n = len(arr)
    last = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last 

    return arr   




def main():
    num = [1,2,3,4,5,6,7]
    result = rightRotateArrayByOnePlace(num)
    print(result)

main()

