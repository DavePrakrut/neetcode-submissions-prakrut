class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countc={}
        for i in range(len(nums)):
            countc[nums[i]]=1+countc.get(nums[i],0)
        return sorted(countc,key=lambda x:countc[x],reverse=True)[:k] 

        