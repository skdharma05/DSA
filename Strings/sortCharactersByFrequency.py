from collections import Counter
class SortCharacterByFrequency:
    def optimal(self,s):
        freq = Counter(s)
        bucket = [[] for _ in range(len(s)+1)]

        for ch , count in freq.items():
            bucket[count].append(ch)
        result =[]
        for i in range(len(bucket)-1,0,-1):
            for ch in bucket[i]:
                result.append(ch*i)
        return "".join(result)

s = "tree"
solution = SortCharacterByFrequency()
print(solution.optimal(s)) 