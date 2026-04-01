def FindCount(nums):
    evencount = 0
    oddcount = 0
    for num in nums:
        if num & 1 ==0:
            evencount+=1
        else:
            oddcount+=1
    return [evencount,oddcount]

nums = set(list(map(int,input("Enter numbers").split())))
print("Even and Odd count : ",FindCount(nums))