import sys

def main():
    num = int(input("Enter a number between 1 and 9,999:\n"))
    if num == 0:
        print("Roman Numerals: ")
        print("Bye.")
        sys.exit()
    else:
        print("Roman Numerals:", roman_num(num))
        main()
    
def roman(num, one, five, ten):
    if (num >= 1) and (num <=9):
        if num in range(1, 4):
            x = num * one
        elif num == 4:
            x = one + five
        elif num in range(5, 9):
            x = five + ((num - 5) * one)
        elif num == 9:
            x = one + ten
        return x
    else:
        return ""
        
def roman_num(num):
    numbers = []
    romanNumeral = []
    while num != 0:
        numbers.append(num % 10)
        num = num // 10
    for i in numbers:
        if numbers.index(i) == 0:
            romanNumeral.append(roman(numbers[0], "I", "V", "X"))
        elif numbers.index(i) == 1:
            romanNumeral.append(roman(numbers[1], "X", "L", "C"))
        elif numbers.index(i) == 2:
            romanNumeral.append(roman(numbers[2], "C", "D", "M"))
        elif numbers.index(i) == 3:
            romanNumeral.append(roman(numbers[3], "M", "v", "x"))
    
    romanNumeral = romanNumeral[::-1]
    return "".join(romanNumeral)

if __name__ == "__main__":
    print("Roman Number Generator. Enter 0 to quit.")
    main()