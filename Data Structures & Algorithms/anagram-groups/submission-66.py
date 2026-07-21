class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g=defaultdict(list)
        for words in strs:
            key=tuple(sorted(words))
            g[key].append(words)
        return list(g.values())    
        