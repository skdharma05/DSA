def largestBrutal(num):

    n = sorted(num)
    return n[-1]


def largesstOptimal(num):
    largest = num[0]
    for i in range(len(num)):
        if num[i]>largest:
            largest = num[i]
    
    return largest




def main():

    num = [1,4,7,5,45,87,34]
    result = largesstOptimal(num)
    print(result)

main()