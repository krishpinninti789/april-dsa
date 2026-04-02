def MaxOnes(nums):
    maxi = len(max("".join(map(str, nums)).split('0')))
    return maxi

nums = list(map(int,input("Enter 0's and 1's: ").split()))
print("Most consecutive 1's are : ",MaxOnes(nums))