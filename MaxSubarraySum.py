def maxSubArray(nums):
        
    current_sum =0
    max_sum = float("-inf")
    for x in range(len(nums)):
        current_sum = max(nums[x],current_sum+nums[x])
        max_sum = max(max_sum,current_sum)
    return max_sum

ls = list(map(int,input("Enter numbers: ").split()))
print(maxSubArray(ls))