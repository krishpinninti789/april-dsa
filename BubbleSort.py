def BubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] > nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    print(nums)            
    
nums = list(map(int,input("ENter the nums: ").split()))
BubbleSort(nums)