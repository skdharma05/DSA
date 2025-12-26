def longestSubStrWithoutRepeatingChar(s):
    if s==None and len(s) == 0:
        return 0
    if len(s)==1:
        return 1
    left =0
    ans = 0
    charSet = set()

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        ans = max(ans,right - left +1)
    
    return ans

def main():
    s = "abcabcbb"
    result = longestSubStrWithoutRepeatingChar(s)
    print(result)
main()