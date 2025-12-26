from collections import  defaultdict

class GroupAnagram:
    def group_anagrams(self, strs):
        if not strs:
            return []
        
        ans_map = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = '#'.join(map(str,count))
            ans_map[key].append(s)
        
        return list(ans_map.values())
    
    
groupAnagram = GroupAnagram()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagram.group_anagrams(strs)
print(f"Grouped Anagrams: {result}")
