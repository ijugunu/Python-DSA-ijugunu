class Solution: 
    def selectionSort(self, arr):
        n=len(arr)
        for i in range(n):
            min_idx=i
            for j in range(i+1,n):
                if arr[j]<=arr[min_idx]:
                    min_idx=j
            
            temp=arr[min_idx]
            arr[min_idx]=arr[i]
            arr[i]=temp
        
        return arr    