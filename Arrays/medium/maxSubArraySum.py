def brutMaxSubArraySum(num):#better solutionn

    maxi = float('-inf')
    for i in range(len(num)):
        sumi =0
        for j in range(i,len(num)):
            sumi = sumi+num[j]
            maxi = max(sumi , maxi) 
    return maxi

def opiMaxSubArraySum(num): #kadanes algo
    maxi = float('-inf')
    sumi =0
    for i in range(len(num)):
        sumi = sumi + num[i]
        if sumi >maxi:
            maxi = max(sumi,maxi)
        if sumi <0:
            sumi =0
    

    return maxi


def main():
     num = [-2,-3,4,-1,-2,1,5,-3]

     result = opiMaxSubArraySum(num)
     print(result)

main()
