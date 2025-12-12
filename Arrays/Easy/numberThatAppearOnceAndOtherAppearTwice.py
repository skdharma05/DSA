def getSingleElement(arr):
    xor = 0

    # XOR all elements — duplicates cancel out
    for num in arr:
        xor ^= num

    return xor

def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)
main()