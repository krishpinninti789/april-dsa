def SecondLarge(nums):
    max1 = nums[0]
    max2 = nums[1]
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
    return max2
    
    
    
nums = list(map(int,input("Enter the numbers: ").split()))
print(SecondLarge(nums))