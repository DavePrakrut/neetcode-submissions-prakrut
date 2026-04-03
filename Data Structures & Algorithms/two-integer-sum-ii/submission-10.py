class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            addsum=numbers[r]+numbers[l]
            if addsum>target:
                r-=1
            elif addsum<target:
                l+=1
            else:
                return [l+1,r+1]        
        