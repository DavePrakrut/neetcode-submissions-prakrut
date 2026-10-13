from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tk=Counter(nums)
        return sorted(tk,key=lambda x:tk[x],reverse=True)[:k]


        