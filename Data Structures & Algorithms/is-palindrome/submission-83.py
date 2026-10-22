class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for s in s:
            if s.isalnum():
                res+=s.lower()
        return res==res[::-1]        
        