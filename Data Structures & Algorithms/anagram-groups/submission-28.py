class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for words in strs:
            key=tuple(sorted(words))
            d[key].append(words)
        return list(d.values())   
        