def twoscomp(binary):
    converted = []
    for bit in binary:
        if bit == "1":
            converted += "0"
        else:
            converted += "1"
    for i in range(len(converted)-1, -1, -1):
        if converted[i] == "0":
            converted.pop(i)
            converted.insert(i, "1")
            break
        else:
            converted.pop(i)
            converted.insert(i, "0")
    return "".join(converted)

if __name__ == "__main__":
    print("Welcome to Two's Complement Creator")
    userBinary = input("Enter a Binary Value:\n")
    
    print("In Two's Complement:")
    print(twoscomp(userBinary))
    