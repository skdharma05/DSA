def fizzBuzz(nums):

    ans=[]

    for i in range(len(nums)):
        if nums[i] % 3 == 0 and nums[i] % 5 == 0:
            ans.append("fizzBuzz")
        elif nums[i] % 3 == 0:
            ans.append("fizz")
        elif nums[i] % 5 == 0:
            ans.append("buzz")
        else:
            ans.append(nums[i])

    return ans
def main():
    nums = [1,2,3,4,5,6,7,8,9,10]
    result = fizzBuzz(nums)
    print(f"The Fizz Buzz is : {result}")
main()