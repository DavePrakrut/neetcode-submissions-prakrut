class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in range(len(nums)):
            c[nums[i]]=1+c.get(nums[i],0)
        return sorted(c,key=lambda x:c[x],reverse=True)[:k]    
        