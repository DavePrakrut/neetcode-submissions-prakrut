class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tk={}
        for i in range(len(nums)):
            tk[nums[i]]=1+tk.get(nums[i],0)
        return sorted(tk,key=lambda x:tk[x],reverse=True)[:k]   

        