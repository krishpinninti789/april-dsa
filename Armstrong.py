def isArmstring(num):
    try:
        power =  len(str(num))
        digit = 0
        for i in range(power):
            digit+=int(str(num)[i]) ** power
        
        return "Armstrong number" if digit == num else "Not Armstrong"
    except:
        print("Given number is not string ,you are using lenght")
        
    
num = int(input("Enter number: "))
print(isArmstring(num))