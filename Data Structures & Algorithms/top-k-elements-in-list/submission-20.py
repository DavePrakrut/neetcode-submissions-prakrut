class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countk={}
        for i in range(len(nums)):
            countk[nums[i]]=1+countk.get(nums[i],0)
        return sorted(countk,key=lambda x:countk[x],reverse=True)[:k]    
        