class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=self.nextgreater(nums2)
        result=[]
        for num in nums1:
            ind=nums2.index(num)
            result.append(ans[ind])
        return result    

    def nextgreater(self,num2):
        n=len(num2)
        ans=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and num2[i]>=stack[-1]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(num2[i])
        return ans