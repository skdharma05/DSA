def minWindowSubStr(s,t):
    if len(s)==0 or len(t)==0 or len(s) < len(t):
        return ""
    chMp = {}
    for ch in t:
        chMp[ch] = chMp.get(ch ,0)+1

    required = len(chMp)
    left =0
    create =0

    window={}
    ans = [float('inf'),0,0]

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c,0)+1

        if c in chMp and window[c] == chMp[c]:
            create+=1

        while left <= right and create == required:
            if ( right -left +1)< ans[0]:
                ans = [right-left+1,left,right]

            start_char = s[left]
            window[start_char]-=1
            if start_char in chMp and window[start_char]< chMp[start_char]:
                create-=1

            left+=1
        
    if ans [0] == float('inf'):
        return ""
    return s[ans[1]:ans[2]+1]

def main():
    s = 'ADOBECODEBANC'
    t = 'ABC'
    result = minWindowSubStr(s,t)
    print(result)
main()
