def ReverseString(str1):
    rev = ''
    for i in range(len(str1)-1,-1,-1):
        rev += str1[i]
    return rev
               
str1 = input("Enter a string: ")
print(ReverseString(str1))