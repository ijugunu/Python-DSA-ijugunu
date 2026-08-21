class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.solve(nums,0,[],res)
        return res

    def solve(self,nums,ind,subset,res):
        if ind>=len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[ind])
        self.solve(nums,ind+1,subset,res)
        subset.pop()
        self.solve(nums,ind+1,subset,res)
                            
