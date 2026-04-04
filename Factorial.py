def GiveFact(num):
    i=1
    fact = 1
    while i <=num:
        fact *= i
        i+=1
    return fact   
    
num = int(input("Enter a number: "))
print(GiveFact(num))