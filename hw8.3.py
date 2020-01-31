import sys

def main():
    num = int(input("Enter a number between 1 and 9,999:\n"))
    if num == 0:
        print("Bye.")
        sys.exit()
    else:
        roman_num(num)
    
def roman(num, one, five, ten):
    if (num >= 1) and (num <=9):
        if num in range(1, 4):
            x = num * one
        elif num == 4:
            x = one + five
        elif num == 5:
            x = five
        elif num in range(6, 9):
            x = five + ((num - five) * one)
        elif num == 9:
            x = one + ten
        return x
    else:
        return ""
        
def roman_num(num):
    romanNumeral = []
    if num >= 1000:
        thousand = num // 1000
        num = num % 1000
        fivehundred = num // 500
        num = num % 500
        hundred = num // 100
        num = num % 100
        fifty = num // 50
        num = num % 50
        ten = num // 10
        num = num % 10
        five = num // 5
        num = num % 5
        one = num
        b = (thousand * "M") + (fivehundred * "D")
        romanNumeral.append(b)
        hundreds = roman(hundred, "C", "D", "M")
        romanNumeral.append(hundreds)
        tens = roman(ten, "X", "L", "C")
        romanNumeral.append(tens)
        fives = roman(five, "V", "X", "L")
        romanNumeral.append(fives)
        ones = roman(one, "I", "V", "X")
        romanNumeral.append(ones)
    elif (num >= 500) and (num <= 999):
        fivehundred = num // 500
        num = num % 500
        hundred = num // 100
        num = num % 100
        fifty = num // 50
        num = num % 50
        ten = num // 10
        num = num % 10
        five = num // 5
        num = num % 5
        one = num
        b = (fivehundred * "D")
        romanNumeral.append(b)
        hundreds = roman(hundred, "C", "D", "M")
        romanNumeral.append(hundreds)
        tens = roman(ten, "X", "L", "C")
        romanNumeral.append(tens)
        fives = roman(five, "V", "X", "L")
        romanNumeral.append(fives)
        ones = roman(one, "I", "V", "X")
        romanNumeral.append(ones)
    elif (num >= 100) and (num <= 499):
        hundred = num // 100
        num = num % 100
        fifty = num // 50
        num = num % 50
        ten = num // 10
        num = num % 10
        five = num // 5
        num = num % 5
        one = num
        hundreds = roman(hundred, "C", "D", "M")
        romanNumeral.append(hundreds)
        tens = roman(ten, "X", "L", "C")
        romanNumeral.append(tens)
        fives = roman(five, "V", "X", "L")
        romanNumeral.append(fives)
        ones = roman(one, "I", "V", "X")
        romanNumeral.append(ones)
    elif (num >= 10) and (num <= 99):
        fifty = num // 50
        num = num % 50
        ten = num // 10
        num = num % 10
        five = num // 5
        num = num % 5
        one = num
        tens = roman(ten, "X", "L", "C")
        romanNumeral.append(tens)
        fives = roman(five, "V", "X", "L")
        romanNumeral.append(fives)
        ones = roman(one, "I", "V", "X")
        romanNumeral.append(ones)
    else:
        romanNumeral = roman(num, "I", "V", "X")
    
    print("".join(romanNumeral))
    main()

if __name__ == "__main__":
    print("Roman Number Generator. Enter 0 to quit.")
    main()