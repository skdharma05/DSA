def brute(nums):
    n= len(nums)
    longest =1
    for i in range(n):
        num = nums[i]
        cunt =1
        while num + 1 in nums:
            num +=1
            cunt +=1
        longest = max(longest,cunt)
    return longest

def better(nums):
    n= len(nums)
    cunt =0
    longest = 1
    lastSmall =float('-inf')
    if n ==0:
        return 0
    
    nums.sort()

    for i in range(n):
        if nums[i]-1 == lastSmall:
            cunt+=1
            lastSmall = nums[i]
        elif nums[i]!=lastSmall:
            cunt =1
            lastSmall = nums[i]
        longest = max(longest,cunt)
    return longest

def optimal(nums):
    num_set = set(nums)
    longest =1
    
    if not nums:
        return 0
    for num in num_set:
        if num -1 not in num_set:
            currentValue = num
            length =1
            while currentValue+1 in num_set:
                currentValue +=1
                length+=1
            longest = max(longest,length)
        
    return longest

def main():
    num = [1, 2, 3, 1, 2, 1, 1, 5, 2, 1, 4, 1, 1]   
    result = optimal(num)
    print(result)
main() 