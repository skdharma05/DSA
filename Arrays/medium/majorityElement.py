def majorElement(num):
    n = len(num)
    count =0
    element =0
    for i in range(n):
        if count ==0:
            count=1
            element = num[i]
        elif element == num[i]:
            count+=1
        else:
            count-=1

    cnt = num.count(element)
    if cnt>(n//2):
        return element
    
    return -1

def main():
    num = [1,2,3,1,2,1,1,5,2,1,4,1,1]
    result = majorElement(num)
    print(result)
main()