class Solution:
    def maxConsecBits(self, arr):
        #code here 
        mb0 = 0
        mb1=0
        cc0 = 0
        cc1=0
        for ele in arr:
            if ele==0:
                cc1=0
                cc0+=1
                mb0=max(mb0,cc0)
            else:
                cc0=0
                cc1+=1
                mb1 = max(mb1,cc1)
        return max(mb1,mb0)
                