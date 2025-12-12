def charcterReplacement(s,k):
    occurance = [0]*26
    left =0
    result = 0
    maxOccurance =0

    for right in range(len(s)):
        occurance[ord(s[right])-ord('A')] +=1
        maxOccurance=max(maxOccurance,occurance[ord(s[right])-ord('A')])

        if(right-left +1 )-maxOccurance>k:
            occurance[ord(s[left])-ord('A')]-=1
            left+=1

        result = max(result,right-left+1)

    return result

def main():
    s = "ABAB"
    res = charcterReplacement(s,2)
    print(res)
main()