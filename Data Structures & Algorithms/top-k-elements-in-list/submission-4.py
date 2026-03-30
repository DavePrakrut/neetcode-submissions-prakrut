class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countA={}
        for i in range(len(nums)):
            countA[nums[i]]=1+countA.get(nums[i],0)
        return sorted (countA, key=lambda x: countA[x], reverse=True)[:k]
            