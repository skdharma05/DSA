def leftRotateArrayByDPlace(arr, d):
    n = len(arr)
    d = d%n
    def reverse(start,end):
        while start<end:
            arr[start],arr[end] = arr[end],arr[start]
            start+=1
            end-=1

    reverse(0,d-1) #[1,2,3,4,5,6,7] -> [2,1,3,4,5,6,7]
    reverse(d,n-1) #[2,1,3,4,5,6,7] -> [2,1,7,6,5,4,3]
    reverse(0,n-1) #[2,1,7,6,5,4,3] -> [3,4,5,6,7,1,2]

    return arr


def main():
    num = [1,2,3,4,5,6,7]
    result = leftRotateArrayByDPlace(num,2)
    print(result)

main()



    