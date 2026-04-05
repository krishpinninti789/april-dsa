from collections import Counter

def Anagrams(s1,s2):
    if len(s1)!=len(s2):
        return False
    return Counter(s1) == Counter(s2)
               
s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
print(Anagrams(s1,s2))
