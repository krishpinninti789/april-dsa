def CheckPrime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count+=1
    return "Prime" if count ==2 else "not a Prime"
  
num = int(input("Enter a number: "))
print("Number is ",CheckPrime(num))