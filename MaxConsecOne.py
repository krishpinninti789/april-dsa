class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cc=0
        mc=0
        j=0
        while(j<len(nums)):
            if nums[j]==1:
                cc+=1
            else:
                mc = max(mc,cc)
                cc=0
            j+=1
        return max(mc,cc)
        