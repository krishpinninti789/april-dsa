def GetFrequency(nums):
    dict1 = {}
    for i in nums:
        if i not in dict1:
            dict1[i]= 1
        else:
            dict1[i]+=1
    return dict1
    
    
    
    
nums = list(map(int,input("Enter the nums : ").split()))
print(GetFrequency(nums))