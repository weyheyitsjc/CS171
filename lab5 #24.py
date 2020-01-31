letter = input("Enter a letter from 'a-z'")

try:
    letter = int(letter)
    print("That is not a letter from 'a-z'")
except:
    try:
        letter = float(letter)
        print("That is not a letter from 'a-z'")
    except:
        if len(letter) == 1:
            print("Good job!")
        else:
            print("That is not a letter!")
    
