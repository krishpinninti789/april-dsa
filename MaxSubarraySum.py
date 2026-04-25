class Solution(object):
    def maximumSubarraySum(self, nums, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        w_sum = 0
        max_sum = 0
        left = 0
        
        for right in range(len(nums)):
            # expand window
            w_sum += nums[right]
            freq[nums[right]] += 1
            
            # shrink if window > k
            if right - left + 1 > k:
                w_sum -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            
            # valid window check
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, w_sum)
        
        return max_sum
