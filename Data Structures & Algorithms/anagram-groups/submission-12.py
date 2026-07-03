from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for word in strs:
            abc = [0] * 26
            for letter in word:
                abc[ord(letter) - ord('a')] += 1
            count[tuple(abc)].append(word)
        
        return list(count.values())