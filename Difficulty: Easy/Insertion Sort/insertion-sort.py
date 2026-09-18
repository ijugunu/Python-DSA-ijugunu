class Solution:
    def insertionSort(self, arr):
        n=len(arr)
        for i in range(n):
            j=i
            while j>=1 and arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1
                