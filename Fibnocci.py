def Fib(limit):
    fib = [0,1]
    if limit == 1:
        return fib[0]
    if limit == 2:
        return fib
    else:
        for i in range(2,limit):
            fib.append(fib[i-2]+fib[i-1])      
    return fib
    
limit = int(input("Enter a limit: "))
print("Fib is : ",Fib(limit))