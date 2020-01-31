import sys
def main():
    zipcode = input("Enter Zip Code (exit to quit):\n")
    if zipcode.lower() == "exit":
        print("Thanks for using me.")
        sys.exit()
    else:
        print("Bar Code:")
        print(barcode(zipcode))
        main()

def checksum(zipcode):
    zipcode = [int(i) for i in str(zipcode)]
    total = sum(zipcode)
    numTill = 0
    while total % 10 != 0:
        numTill += 1
        total += 1
    return str(numTill)

def barcode(zipcode):
    remainder = checksum(zipcode)
    zipcode = list(zipcode)
    #remainder = int(remainder)
    #zipcode = [int(i) for i in str(zipcode)]
    #if int(remainder) != 0:
    zipcode.append(remainder)
    barCode = ["|"]
    for num in zipcode:
        if num.isdigit():
            if num == "1":
                barCode.append(":::||")
            elif num == "2":
                barCode.append("::|:|")
            elif num == "3":
                barCode.append("::||:")
            elif num == "4":
                barCode.append(":|::|")
            elif num == "5":
                barCode.append(":|:|:")
            elif num == "6":
                barCode.append(":||::")
            elif num == "7":
                barCode.append("|:::|")
            elif num == "8":
                barCode.append("|::|:")
            elif num == "9":
                barCode.append("|:|::")
            elif num == "0":
                barCode.append("||:::")
    barCode.append("|")
    return "".join(barCode)
    
if __name__ == "__main__":
    print("Welcome to Bar Code Generator")
    main()