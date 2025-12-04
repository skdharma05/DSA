def moveZeros(arr):
    count =0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[count]=arr[count],arr[i]
            count+=1
    return arr


def main():
    num = [1,0,3,0,5,0,7]
    result = moveZeros(num)
    print(result)
main()
