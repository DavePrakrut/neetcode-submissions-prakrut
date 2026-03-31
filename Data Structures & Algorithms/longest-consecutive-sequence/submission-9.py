class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seenset=set(nums)
        longest = 0
        for i in seenset:
            if i-1 not in seenset:
                length=0
                while i+length in seenset:
                    length+=1
                longest=max(length,longest)
        return longest            
        