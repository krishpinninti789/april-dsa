class Solution:
    def maxOnes(self, arr, k):
        # code here
        left = 0
        maxans = 0
        zc=0
        for right in range(len(arr)):
            if arr[right]==0:
                zc+=1
            if zc>k:
                if arr[left]==0:
                    zc-=1
                left+=1
            
        return len(arr)-left
        
