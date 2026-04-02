def MaxOnes(nums):
    max_count = 0
    count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

nums = list(map(int,input("Enter 0's and 1's: ").split()))
print("Most consecutive 1's are : ",MaxOnes(nums))