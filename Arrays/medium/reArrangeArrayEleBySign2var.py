def brutreArrangeElemBysign(num):#brute
    n = len(num)
    posi =[]
    negi =[]
    for i in range(len(num)):
        if num[i]>0:
            posi.append(num[i])
        else:
            negi.append(num[i])
    for i in range(n//2):
        num[2 * i]=posi[i] 
        num[2 * i + 1] = negi[i]  

    return num


def reArrangeElemBysign(num):#optimal
    n = len(num)
    posi =0
    negi =1
    ans =[0]*n
    for i in range(n):
        if num[i]>0:
            ans[posi]= num[i]
            posi+=2
        else:
            ans[negi] = num[i]
            negi+=2
    return ans


def main():
     num = [3,1,-2,-5,2,-4]

     result = reArrangeElemBysign(num)
     print(result)

main()
