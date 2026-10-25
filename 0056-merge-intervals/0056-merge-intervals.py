class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        intervals.sort()
        ans=[]
        ans.append(intervals[0])
        for i in range(1,n):
            if ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])
            else:
                #ans[-1][0]=min(ans[-1][0],intervals[i][0])
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
        return ans            
        