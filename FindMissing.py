def FindMissing(nums):
    missingNums = []
    max1 = max(nums)
    for i in range(1,max1):
        if i not in nums:
            missingNums.append(i)
    return missingNums
   

nums = list(map(int,input("Enter the nums in sorted: ").split()))
print(FindMissing(nums))
    