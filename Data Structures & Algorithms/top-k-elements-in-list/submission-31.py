class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk={}
        for i in range(len(nums)):
            topk[nums[i]]=1+topk.get(nums[i],0)
        return sorted (topk,key=lambda x:topk[x],reverse=True)[:k]    
        