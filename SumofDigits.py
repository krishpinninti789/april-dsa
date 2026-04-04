def GiveSum(num):
    
    sum1 = 0
    while num!=0:
        sum1+=num %10
        num = num//10
    return sum1
  
    
num = int(input("Enter a number: "))
print(GiveSum(num))