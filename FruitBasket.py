class Solution:
    def totalElements(self, arr):
        # Code here
        hmap = {}
        ans = 0
        left = 0
        for right in range(len(arr)):
            hmap[arr[right]] = hmap.get(arr[right],0)+1
            while len(hmap)>2:
                hmap[arr[left]]-=1
                if hmap[arr[left]]==0:
                    hmap.pop(arr[left])
                left+=1
            ans = max(ans,right-left+1)
        return ans