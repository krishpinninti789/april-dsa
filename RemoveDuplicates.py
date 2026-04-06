def RemoveDup(nums):
    return list(set(nums))
      
ls = list(map(int,input("Enter numbers: ").split()))
print(RemoveDup(ls))