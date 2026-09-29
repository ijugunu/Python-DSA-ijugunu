class Solution:
    def candy(self, ratings: list[int]) -> int:
        n=len(ratings)
        candy1=[-1]*n
        candy2=[-1]*n
        candy1[0]=1
        candy2[-1]=1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candy1[i]=candy1[i-1]+1
            else:
                candy1[i]=1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candy2[i]=candy2[i+1]+1
            else:
                candy2[i]=1
        res=0
        for i in range(n):
            res+=max(candy1[i],candy2[i])
        return res                            
