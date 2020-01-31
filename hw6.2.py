import sys
print("Welcome to Binary Printer")
print("Enter exit to quit at any time.")

def getInt():
    while True:
        uinput = input("Enter a Positive Int:\n")
        if uinput.lower() == "exit":
            sys.exit()
        elif ubits.lower == "exit":
            sys.exit()
        else:
            print("Not a Number.")
            uinput = input("Enter a Positive Int:\n")
        ubits = input("Number of Bits:\n")
        intinput = int(uinput)
        intbits = int(ubits)
        if uinput.lower() == "exit":
            sys.exit()
        elif ubits.lower == "exit":
            sys.exit()
        else:
            print("Not a Number.")
            uinput = input("Enter a Positive Int:\n")
            continue
    return integer

def binaryStr(num, bits):
    binarybits = []
    while num != 0:
        num = num // 2
        binarybits.append(0 if num % 2 == 0 else 1)
        
    binarybits = [str(i) for i in binarybits]
        
    if len(binarybits) != bits:
        for i in range(0, (len(binarybits)) - bits):
                binarybits.pop(0)
        for i in range(1, (bits - len(binarybits)) + 1):
                binarybits.insert(0, "0")
    return "".join(str(i) for i in binarybits)
    
getInt()
print("As Binary:", binaryStr(getInt(), intbits))
    