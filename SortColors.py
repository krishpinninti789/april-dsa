def sort012(self, arr):
        # code here
        n= len(arr)
        low = 0
        mid = 0
        high = n-1
        for i in range(n):
            while mid<=high:
                if arr[mid]==0:
                    arr[mid]=arr[low]
                    arr[low]=0
                    low+=1
                    mid+=1
                elif arr[mid]==1:
                    mid+=1
                else:
                    arr[mid]=arr[high]
                    arr[high]=2
                    high-=1
        return arr
