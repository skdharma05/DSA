def longestCommonPrefix(arr):

    if arr == None and len(arr)==0:
        return ""
    
    prefix=arr[0]
    for s in arr:
        while s.find(prefix)!=0:
            prefix = prefix[:-1]
            if prefix =="":
                return ""
    return prefix
def main():
    arr = ["flow","flower","float","flight"]
    result = longestCommonPrefix(arr)
    print(f"The longest common prefix: {result}")
main()