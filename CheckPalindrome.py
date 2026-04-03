def CheckPalindrome(s1):
    i=0
    j=len(s1)-1
    while i<j:
        if s1[i]!=s1[j]:
            return False
        i+=1
        j-=1
    return True 
    
str1 = input("Enter the string: ")
print(CheckPalindrome(str1))