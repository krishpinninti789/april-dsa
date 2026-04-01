def Maximum(numbers):
    maxNum = -999999
    for number in numbers:
        if number >maxNum:
            maxNum = number
    return maxNum

numbers = list(map(int, input("Enter numbers: ").split()))
print(Maximum(numbers))