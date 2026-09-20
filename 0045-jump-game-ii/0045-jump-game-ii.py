class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        jump=0
        L,R=0,0
        while R<n-1:
            farthest=0
            for i in range(L,R+1):
                farthest=max(farthest,i+nums[i])
            L=R+1
            R=farthest
            jump+=1
        return jump            