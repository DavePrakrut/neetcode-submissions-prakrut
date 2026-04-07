class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countc,countt={},{}
        for i in range(len(s)):
            countc[s[i]]=1+countc.get(s[i],0)
            countt[t[i]]=1+countt.get(t[i],0)
        return countc==countt        
        