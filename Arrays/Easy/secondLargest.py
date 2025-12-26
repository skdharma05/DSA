
def secondLargestOptimal(num):
    largest = float('-inf')
    secondLargest=float('-inf')
    for i in range(len(num)):
        if num[i]>largest:
            secondLargest= largest
            largest = num[i]
        
        elif num[i]>secondLargest and num[i] != largest:
            secondLargest=num[i]
    
    return secondLargest

def secondSmallest(num):
    smallest = float('inf')
    secondSmallest=float('inf')

    for i in range(len(num)):
        if num[i]<smallest:
            secondSmallest = smallest
            smallest = num[i]

        elif num[i]<secondSmallest and num[i] !=smallest:
            secondSmallest=num[i]
    
    return secondSmallest

def main():

    num = [1,4,7,5,45,87,74]
    result = secondLargestOptimal(num)
    print(result)

main()