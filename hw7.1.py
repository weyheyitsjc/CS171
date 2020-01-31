import sys
print("Welcome to Fraction Simplifier")
print('Type "exit" to quit.')

def main():
    num = input("Enter Fraction (Int/Int):\n")
    if num.lower() == "exit":
        print("Bye.")
        sys.exit()
    else:
        fractionInt(num)
        
def fractionInt(num):
    num = num.split("/")
    numerator = num[0]
    denominator = num[1]
    gcd(numerator, denominator, num)

def gcd(numerator, denominator, num):
    numerator = int(numerator)
    denominator = int(denominator)
    if numerator > denominator:
        remain = (numerator % denominator)
        if remain == 0:
            gcdd = denominator
        elif remain == 1:
            gcdd = 1
        else:
            gcd(numerator, remain, num)
    elif denominator > numerator:
        remain = (denominator % numerator)
        if remain == 0:
            gcdd = numerator
        elif remain == 1:
            gcdd = 1
        else:
            gcd(denominator, remain, num)
    numerator = (int(num[0]) // gcdd)
    denominator = (int(num[1]) // gcdd)
    print("Simplified Fraction")
    if (numerator % denominator) == 0:
        print(numerator // denominator)
    else:
        print(str(numerator) + "/" + str(denominator))
    main()
main()