def GivePrimes(num):
    ls = []
    for i in range(1,num+1):
        count = 0
        for j in range(1,i+1):
            if i % j ==0:
                count +=1
        if count ==2:
            ls.append(i)
    return ls
   
num = int(input("Enter a number: "))
print("PRimes are",GivePrimes(num))
print("Count is : ",len(GivePrimes(num)))