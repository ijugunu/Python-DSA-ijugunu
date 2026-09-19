class Solution:
    def mergeSort(self, arr, l, r):
        # code here
        if l >= r:
            return arr[l:r+1]
        
        mid=(l+r)//2
        
        left=self.mergeSort(arr,l,mid)
        right=self.mergeSort(arr,mid+1,r)
        
        merged=self.merge_procedure(left,right)
        
        arr[l:r+1] = merged

        return merged    
    
    def merge_procedure(self,left,right):
        n=len(left)
        m=len(right)
        i,j=0,0
        result=[]
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        
        while i<n:
            result.append(left[i])
            i+=1
        while j<m:
            result.append(right[j])
            j+=1
        
        return result    