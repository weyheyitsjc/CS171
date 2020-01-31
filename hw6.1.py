import math
print("Welcome to Prime Generator")

def check_int():
    while True:
        try:
            userInput = int(input("Enter a number:\n"))
            break
        except:
            continue
    return userInput

def prime(number):
    primeList = []
    i = 2
    while i <= math.sqrt(number):
        if i in range(2, number + 1):
            for i in range(i * 2, number + 1, i):
                primeList.append(i)
        i += 1
    for i in primeList:
        print(i, "is a prime number.")
    
nums = check_int()
prime(nums)
