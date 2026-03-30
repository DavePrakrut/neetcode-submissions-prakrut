class Solution:
    def groupAnagrams(self, strs):
        h = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            h[key].append(word)

        return list(h.values())  
        