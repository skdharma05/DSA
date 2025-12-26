# to check the array is sorted and rotated.

def sortedArray(num):
    count =0
    for i in range(len(num)):
        if num[i]>num[(i+1) % len(num)]: # its check if next num in i is samller then previous num its break and check next num.
            count+=1
        
        if count>1: # if the count graterthan 1 it should return false.
            return False
    
    return True

def main():
    # num = [1,2,3,4,5]
    num = [3,4,5,6,1,2]
    # num= [9,8,7,1,5,8,4]

    result = sortedArray(num)
    print(result)
main()