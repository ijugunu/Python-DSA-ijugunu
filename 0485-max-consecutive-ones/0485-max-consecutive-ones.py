class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n=len(nums)
        count=0
        maxi=0
        for i in range(n):
            if nums[i]==1:
                count+=1
            else:
                count=0
            maxi=max(maxi,count)
        return maxi            