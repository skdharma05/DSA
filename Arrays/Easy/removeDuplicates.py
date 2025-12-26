# this program will remove the duplicates from the sorted array.

# brute force time complexity for this is N logn + N ,space complexity is O(N).
def removeDupliicateFromSortedArray(nums):
    duplicatSet = set() # create a empty set
    index=0

    for num in nums:
        if num not in duplicatSet:
            duplicatSet.add(num) # if not in set then add to set
            nums[index] = num 
            index+=1

    return index

#optimal solution for remove duplicate from an sorted array using two pointers. time complexity is O(N),space complexity is O(1).
def optiamlRemoveDupliicateFromSortedArray(num):
    i =0
    for j in range(len(num)):
        if num[j] != num[i]:
            num[i+1] = num[j]
            i+=1
    return i+1


def main():

    n = [1,1,2,2,3,3]
    ans = optiamlRemoveDupliicateFromSortedArray(n)
    print(ans)

main() 
