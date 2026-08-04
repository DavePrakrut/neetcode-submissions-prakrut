class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kl={}
        for i in range(len(nums)):
            kl[nums[i]]=1+kl.get(nums[i],0)
        return sorted(kl,key=lambda x:kl[x],reverse=True)[:k]    
        